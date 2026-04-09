# SecureApp Sprint - ByteGuard

This project is a secure Flask blog application developed for CYC386 Midterm Lab Exam.

## Security Controls Implemented

- IDOR prevention with object-level authorization checks.
- CSRF protection using Flask-WTF CSRF tokens.
- Clickjacking prevention with `X-Frame-Options` and CSP `frame-ancestors`.
- Secure session cookie configuration.
- CI/CD pipeline with SAST and dependency audit.

## Quick Start

1. Create and activate a Python virtual environment.
2. Install dependencies:
   - `pip install -r requirements.txt`
3. Run app:
   - `python run.py`
4. Open:
   - `http://127.0.0.1:5000`

## Project Structure

- `src/app`: Application source code
- `tests`: Test suite
- `docs`: Security documentation
- `.github/workflows`: CI/CD pipeline
