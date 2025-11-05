# Image Background Remover

A small Flask web app that removes the background from uploaded images and
saves the results to the `results/` folder. This repository contains a
minimal UI (in `templates/index.html`) for uploading images, a simple
server entrypoint (`app.py`) and the folders used for input/output.

The app is intended as a small, local tool for experimenting with image
background removal and as a starting point to build a larger service.

## Features

- Upload an image via the web UI
- Remove the background from the uploaded image and save the result
- Stores original uploads under `uploads/` and processed images under `results/`

## Requirements

- Python 3.8+
- See `requirements.txt` for exact Python packages used by the app

## Quick start

1. Create and activate a virtual environment (recommended):

```bash
python3 -m venv .venv
source .venv/bin/activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python3 app.py
```

4. Open the UI in your browser at http://127.0.0.1:5000 and upload an image.

After a successful run:

- The original file will be in `uploads/`
- The background-removed result will be in `results/` (look for files prefixed with `removed_`)

## Project layout

- `app.py` — Flask application and request handling
- `templates/index.html` — simple upload UI
- `static/style.css` — styling for the web UI
- `uploads/` — where uploaded images are saved
- `results/` — where processed images are saved
- `requirements.txt` — Python dependencies

## Usage notes

- This project is intentionally minimal. It expects a working dependencies
  setup as given in `requirements.txt`. If background removal depends on a
  third-party model or binary, ensure those are installed and available.
- The app stores files locally; if you deploy or expose it publicly, add
  authentication, file size limits, and input validation.

## Troubleshooting

- If the server fails to start, check for missing dependencies or Python
  version mismatches (run `python3 --version`).
- If uploads do not appear in `results/`, check the application log output
  in the terminal where you ran `app.py` for error messages.

## Contributing

Feel free to open issues or pull requests. Small improvements I welcome:

- Add unit tests, CI, or Dockerfile
- Add detailed instructions for the background removal implementation
- Make the UI friendlier and add progress indicators
