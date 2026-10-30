#!/usr/bin/env python3
"""Local provenance estimates, durable decisions, and writer appeals."""

import uuid

from flask import Flask, jsonify, request
from werkzeug.exceptions import RequestEntityTooLarge

import audit
import config
import detector
import scoring
import stylometry

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = config.MAX_REQUEST_BYTES


class _LimiterOff:
    def limit(self, *args, **kwargs):
        return lambda view: view


limiter = _LimiterOff()
if config.RATE_LIMITING_ENABLED:
    from flask_limiter import Limiter
    from flask_limiter.util import get_remote_address

    def rate_limit_key():
        payload = request.get_json(silent=True)
        creator = payload.get('creator_id') if isinstance(payload, dict) else None
        return creator.strip() if isinstance(creator, str) and creator.strip() else get_remote_address()

    limiter = Limiter(key_func=rate_limit_key, app=app,
                      storage_uri=config.RATE_LIMIT_STORAGE, default_limits=[])

    @app.errorhandler(429)
    def rate_limited(exc):
        return _reject('rate_limited', 'Too many submissions. Try again shortly.', 429)


def _reject(error, message, status, creator_id='unknown'):
    """Record bounded rejection metadata, without storing submitted writing."""
    try:
        audit.log_rejection(creator_id=creator_id, reason=error,
                            route=request.path, http_status=status)
    except OSError:
        app.logger.error('Could not persist rejection metadata.')
    return jsonify({'error': error, 'message': message}), status


@app.errorhandler(RequestEntityTooLarge)
def request_too_large(exc):
    return _reject('request_too_large', 'Request body must not exceed 65,536 bytes.', 413)


def _json_object():
    if not request.is_json:
        return None, _reject('json_required', 'Send an application/json request body.', 415)
    payload = request.get_json(silent=True)
    if not isinstance(payload, dict):
        return None, _reject('invalid_json', 'Send a valid JSON object.', 400)
    return payload, None


# The starter's worked example remains the control route.
@app.post('/ping')
def ping():
    payload = request.get_json(silent=True) or {}
    return jsonify({
        'ok': True,
        'you_sent': payload.get('message'),
        'service': 'provenance-guard',
    })


@app.get('/health')
def health():
    return jsonify({
        'ok': True,
        'detector_model': config.DETECTOR_MODEL,
        'detector_loaded': detector._model is not None,
        'rate_limiting': config.RATE_LIMITING_ENABLED,
        'log_entries': len(audit.read_entries()),
    })


@app.post('/submit')
@limiter.limit(f'{config.RATE_LIMIT_PER_MINUTE}/minute;{config.RATE_LIMIT_PER_DAY}/day')
def submit():
    payload, error = _json_object()
    if error is not None:
        return error
    text, creator_id = payload.get('text'), payload.get('creator_id')
    if not isinstance(text, str) or not text.strip():
        return _reject('invalid_text', 'text must be a nonempty string.', 400)
    if len(text) > config.MAX_TEXT_CHARS:
        return _reject('text_too_large', 'text must not exceed 10,000 characters.', 413)
    if len(text.strip()) < config.MIN_TEXT_CHARS or len(stylometry.words(text)) < config.MIN_TEXT_WORDS:
        return _reject('text_too_short', 'text needs at least 20 characters and 5 word tokens.', 400)
    if not isinstance(creator_id, str) or not creator_id.strip() or len(creator_id) > config.MAX_CREATOR_CHARS:
        return _reject('invalid_creator_id', 'creator_id must be a nonempty string of at most 128 characters.', 400)

    content_id = str(uuid.uuid4())
    try:
        model_score = detector.model_signal(text)
        metrics = stylometry.component_metrics(text)
        style_score = metrics['style_score']
        combined = scoring.combine_signals(model_score, style_score)
        guess, label = scoring.score_to_label(combined)
    except (detector.DetectorUnavailable, ValueError, RuntimeError, ImportError):
        app.logger.error('The local detector could not score a submission.')
        return _reject('detector_unavailable', 'The local detector is unavailable. Please try again later.', 503, creator_id)

    try:
        entry = audit.log_decision(
            content_id=content_id, creator_id=creator_id, guess=guess,
            model_score=model_score, style_score=style_score,
            combined_score=combined, label=label, status='decided',
            confidence=combined, style_metrics=metrics,
            text_length=len(text), detector_model=config.DETECTOR_MODEL,
        )
    except OSError:
        return jsonify({'error': 'audit_unavailable',
                        'message': 'The decision could not be saved. Please try again later.'}), 503
    return jsonify(entry)


def _content(content_id):
    """Reconstruct current state from the immutable event history."""
    try:
        uuid.UUID(content_id)
    except (ValueError, TypeError, AttributeError):
        return None
    history = audit.entries_for(content_id)
    original = next((entry for entry in history if entry.get('status') == 'decided'), None)
    if original is None:
        return None
    appeals = [entry for entry in history if entry.get('event') == 'appeal']
    return {**original, 'status': 'under_review' if appeals else original['status'], 'appeals': appeals}


@app.post('/appeal')
def appeal():
    payload, error = _json_object()
    if error is not None:
        return error
    content_id, reasoning = payload.get('content_id'), payload.get('reasoning')
    if not isinstance(content_id, str) or not content_id.strip():
        return _reject('invalid_content_id', 'content_id must be a nonempty UUID string.', 400)
    if not isinstance(reasoning, str) or not reasoning.strip():
        return _reject('invalid_reasoning', 'reasoning must be a nonempty string.', 400)
    if len(reasoning) > config.MAX_REASONING_CHARS:
        return _reject('reasoning_too_large', 'reasoning must not exceed 2,000 characters.', 413)
    try:
        content = _content(content_id)
        if content is None:
            return _reject('content_not_found', 'No submission exists with this content_id.', 404)
        event = audit.log_appeal(content_id, content['creator_id'], reasoning)
    except OSError:
        return jsonify({'error': 'audit_unavailable',
                        'message': 'The appeal could not be saved. Please try again later.'}), 503
    return jsonify({**event, 'message': 'Your appeal has been recorded. This writing is now under review.'})


@app.get('/content/<content_id>')
def get_content(content_id):
    try:
        content = _content(content_id)
    except OSError:
        return jsonify({'error': 'audit_unavailable', 'message': 'Saved decisions are temporarily unavailable.'}), 503
    if content is None:
        return jsonify({'error': 'content_not_found', 'message': 'No submission exists with this content_id.'}), 404
    return jsonify(content)


@app.get('/log')
def get_log():
    limit = request.args.get('limit', type=int)
    entries = audit.read_entries(limit=limit)
    return jsonify({'count': len(entries), 'entries': entries})


def main():
    print(f'Provenance Guard on http://{config.HOST}:{config.PORT}')
    print(f'Local detector: {config.DETECTOR_MODEL}; audit: {config.AUDIT_LOG}')
    app.run(host=config.HOST, port=config.PORT, debug=config.DEBUG)


if __name__ == '__main__':
    main()
