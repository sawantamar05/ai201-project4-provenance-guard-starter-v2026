# Capstone environment and clean-checkout protocol

The capstone uses Path B: a local service started outside the editor, with
committed request records. The server command uses Gunicorn with one process
and one thread on loopback. Gunicorn loads the Flask WSGI callable through
`app:app`; its supported command format and bind option are documented in the
[official Gunicorn settings reference](https://gunicorn.org/reference/settings/).
Flask documents deployment through a WSGI server in its
[deployment guide](https://flask.palletsprojects.com/en/stable/deploying/index.html).

## Observed environment before capstone execution

These facts were inspected without running the detector or a capstone trial:

| Item | Observed value |
| --- | --- |
| Interpreter | Python 3.13.3 |
| Platform | macOS 26.6.2, Apple Silicon arm64 |
| Dependencies | All 40 exact versions in `requirements-lock.txt` match the existing virtual environment |
| Server | Gunicorn 23.0.0, Flask 3.1.3 |
| Model libraries | PyTorch 2.15.0, Transformers 4.57.6 |
| GPT-2 cache revision | `607a30d783dfa663caf39e06633721c8d4cfcd7e` |
| GPT-2 snapshot | Seven files, 550,959,861 bytes total (525.44 MiB) |
| Model weights | `model.safetensors`, 548,105,171 bytes |

The size is the sum of snapshot file sizes, counting each file once. Snapshot
symlinks point to cache blobs; adding snapshot and blob totals would count the
same model twice. Logs and cache metadata are not model files. This cache was
downloaded before the capstone. Reusing it does not demonstrate a new online
download or make dependency installation offline.

## Clean-checkout verification

`scripts/verify_clean_checkout.py` is a verification program, not an existing
successful result. The committed `results/capstone/clean_checkout.json`, after
the program has actually run, records whether all its checks passed. Its
`source_commit` identifies the exact checkout tested.

The program:

1. Clones the current committed repository into a new retained temporary folder.
2. Verifies that the clone contains neither `.venv` nor `.cache`.
3. Creates a fresh virtual environment without system site packages.
4. Installs `requirements-lock.txt`, runs `pip check`, and checks every exact pin.
5. Starts the Gunicorn command in that checkout, using a random loopback port,
   isolated session logs, and the explicitly supplied existing GPT-2 cache.
6. Makes a real submission and appeal, stops the server, starts a new process
   on the same logs, and reads the persisted appealed decision.
7. Confirms request-ID correlation, durable request completion records, timing
   fields, redacted completion logs, and unchanged original audit events.

From the original repository, after committing the capstone code, run:

```bash
.venv/bin/python scripts/verify_clean_checkout.py \
  --model-cache "$PWD/.cache/huggingface" \
  --output "$PWD/results/capstone/clean_checkout.json"
```

The program preserves the temporary clone, package installation output, server
logs, HTTP captures, model inventory, command records, and final checks. It
does not copy the original environment or import its packages. The model cache
is deliberately shared and `HF_HUB_OFFLINE=1` prevents inference from silently
downloading missing files.

Dependency installation normally needs network access. The initial sandbox
inspection could not use the user-level pip cache because it was not writable;
no complete wheelhouse was found. If a complete wheelhouse has been prepared,
passing `--wheelhouse /absolute/path` instead installs with `--no-index`. Do not
describe a run as offline merely because the model cache was reused.

## Earlier Part 2 evidence

`scripts/audit_part2.py` checks the complete Part 2 snapshot, including runtime
hashes, its root criteria file, and the original ten README headings. It should
be run against commit `e7aa922`, rather than the capstone working tree, whose
criteria, runtime, and README have intentionally changed. A local clone can
check out that immutable commit and run the historical auditor there; that
auditor writes its report inside the temporary checkout. Keep the archived
Part 2 report and original input files unchanged in the current repository.
