# Security Test Report - ByteGuard

## 1. Testing Scope

The following were tested:
- IDOR exploitability and authorization enforcement
- CSRF token validation
- Clickjacking protection headers
- SAST and dependency security checks

## 2. Manual Validation (Before/After)

### IDOR
- **Before:** Malicious user could attempt `/post/<other_user_id>/edit`.
- **After:** Server responds `403 Forbidden` for non-owner requests.

### CSRF
- **Before:** Cross-site form submission could trigger state changes.
- **After:** Missing/invalid CSRF token blocks request.

### Clickjacking
- **Before:** Pages could be framed by external sites.
- **After:** `X-Frame-Options: DENY` and CSP `frame-ancestors 'none'` prevent framing.

## 3. Automated Testing

- Unit test executed with `pytest`.
- Bandit SAST scan runs in CI.
- `pip-audit` checks dependencies for known vulnerabilities.
- CodeQL analysis enabled in GitHub Actions.

## 4. CI Security Gate

Pipeline fails if any required job fails (tests, SAST, dependency audit, CodeQL).

## 5. Evidence Collection Checklist

- Attach screenshots of failing attack attempt (IDOR/CSRF).
- Attach response headers screenshot for clickjacking controls.
- Attach GitHub Actions run summary screenshots.

Update: Added CI test evidence section note.
