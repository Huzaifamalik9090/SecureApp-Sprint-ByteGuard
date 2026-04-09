# Security Implementation Report - ByteGuard

## 1. IDOR Mitigation

- **Vulnerable area:** Post edit/delete endpoints.
- **Root cause:** Missing object-level authorization checks.
- **Fix implemented:** Added `_get_owned_post_or_403(post_id)` guard in `post_routes.py` to ensure only the owner can modify/delete a post.
- **Result:** Unauthorized access attempts return HTTP 403.

## 2. CSRF Mitigation

- **Vulnerable area:** Form submissions for login, registration, create/edit/delete post, and logout.
- **Root cause:** State-changing requests without anti-CSRF controls.
- **Fix implemented:** Enabled `Flask-WTF` `CSRFProtect` globally and embedded CSRF token in all forms.
- **Cookie hardening:** `HttpOnly=True`, `SameSite=Lax`.
- **Result:** Forged requests without valid token are rejected.

## 3. Clickjacking Mitigation

- **Vulnerable area:** All rendered pages.
- **Root cause:** Missing anti-framing response headers.
- **Fix implemented:** Global `after_request` middleware sets:
  - `X-Frame-Options: DENY`
  - `Content-Security-Policy: frame-ancestors 'none'; default-src 'self';`
- **Result:** Browser blocks iframe embedding.

## 4. Additional Hardening

- Password hashing using Werkzeug secure hash utilities.
- Input validation via WTForms validators.
- CI/CD integration for automated checks.
