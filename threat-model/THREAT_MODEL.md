# Threat Model - ByteGuard Secure Blog

## DFD Components

- External User
- Flask Web App
- Authentication Module
- Post Service
- SQLite Database
- GitHub Actions CI Pipeline

## STRIDE Analysis

| Component | Threat | Example | Mitigation |
|---|---|---|---|
| Auth Module | Spoofing | Credential stuffing | Password hashing, lockout policy (future) |
| Post Routes | Tampering | IDOR on post edit/delete | Object-level authorization checks |
| Forms | Repudiation | Untracked actions | App logging (future enhancement) |
| Database | Information Disclosure | Unauthorized post access | Owner checks + least privilege |
| Session | Elevation of Privilege | Session misuse | Secure cookie settings + CSRF |
| Browser Rendering | Clickjacking | UI redress in iframe | XFO + CSP frame-ancestors |

## CVSS v3.1 Risk Table

| Vulnerability | Base Score | Severity | Rationale |
|---|---:|---|---|
| IDOR | 8.1 | High | Authenticated user can modify other user data |
| CSRF | 6.5 | Medium | Victim actions can be forced via forged requests |
| Clickjacking | 4.3 | Medium | UI deception without direct data compromise |

## Attack Tree (Textual)

Root Goal: Unauthorized data/action manipulation

1. Compromise object access
   - Guess object IDs
   - Access edit/delete endpoints
   - Bypass missing ownership checks
2. Force user actions
   - Craft malicious external form
   - Trigger victim authenticated request
3. UI redress
   - Embed target in hidden iframe
   - Trick victim into unintended click
