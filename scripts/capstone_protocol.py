"""Frozen capstone inputs and scoring helpers; contains no detector execution."""
from pathlib import Path
import json
import math
import uuid

ROOT = Path(__file__).resolve().parents[1]
CORPUS = json.loads((ROOT / 'data/evaluation_inputs.json').read_text())
HUMAN = sorted(CORPUS['human'], key=lambda row: row['id'])
UNKNOWN_ID = '00000000-0000-4000-8000-000000000099'


def reasoning(index):
    return f'  Capstone review {index}: please consider my drafts.  '


def matrix_cases(creator_id):
    """Ten cases in criteria.md, in the registered order."""
    text = HUMAN[0]['text']
    rows = [
        ('missing text', 400, {'json': {'creator_id': creator_id}}),
        ('empty text', 400, {'json': {'text': '', 'creator_id': creator_id}}),
        ('numeric text', 400, {'json': {'text': 42, 'creator_id': creator_id}}),
        ('missing creator', 400, {'json': {'text': text}}),
        ('blank creator', 400, {'json': {'text': text, 'creator_id': '   '}}),
        ('oversized text', 413, {'json': {'text': 'x' * 10001, 'creator_id': creator_id}}),
        ('malformed JSON', 400, {'data': '{', 'headers': {'Content-Type': 'application/json'}}),
        ('non-object JSON', 400, {'data': '[]', 'headers': {'Content-Type': 'application/json'}}),
        ('non-JSON content type', 415, {'data': 'hello', 'headers': {'Content-Type': 'text/plain'}}),
        ('oversized non-JSON body', 413, {'data': 'x' * 65537, 'headers': {'Content-Type': 'text/plain'}}),
    ]
    return [{'case': i, 'name': name, 'expected_status': status, 'kwargs': kwargs}
            for i, (name, status, kwargs) in enumerate(rows, 1)]


def json_error(record, status):
    body = record.get('response_json')
    return (record.get('status_code') == status and isinstance(body, dict)
            and all(isinstance(body.get(key), str) and bool(body[key].strip())
                    for key in ('error', 'message')))


def successful_submission(record):
    body = record.get('response_json')
    if record.get('status_code') != 200 or not isinstance(body, dict):
        return False
    try:
        uuid.UUID(body['content_id'])
        scores = [body[key] for key in ('confidence', 'model_score', 'style_score', 'combined_score')]
        return (all(not isinstance(x, bool) and isinstance(x, (int, float))
                    and math.isfinite(x) and 0 <= x <= 1 for x in scores)
                and body['confidence'] == body['combined_score']
                and body['status'] == 'decided' and body['guess'] in ('human', 'unsure', 'ai')
                and isinstance(body['label'], str) and bool(body['label'].strip()))
    except (KeyError, TypeError, ValueError, AttributeError):
        return False


def jsonl(path):
    """Return parsed records and explicit malformed-line evidence."""
    rows, errors = [], []
    if not path.exists():
        return [], [{'error': 'missing log', 'path': str(path)}]
    for index, line in enumerate(path.read_text().splitlines(), 1):
        try:
            row = json.loads(line)
            if not isinstance(row, dict):
                raise ValueError('record is not an object')
            rows.append(row)
        except (ValueError, TypeError) as exc:
            errors.append({'line': index, 'error': str(exc)})
    return rows, errors
