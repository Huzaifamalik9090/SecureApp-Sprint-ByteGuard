# Protection Needs Elicitation (PNE) Report - ByteGuard

## 1. Project Context

ByteGuard developed a secure Flask-based blog platform where users can register, authenticate, and manage their own posts.

## 2. Critical Assets

- User credentials (password hashes)
- Session cookies and authentication state
- User-owned posts
- Source code and CI/CD workflow integrity

## 3. Threat Actors

- External unauthenticated attacker
- Authenticated malicious user attempting privilege abuse
- Automated scanners/bots targeting known vulnerabilities

## 4. Protection Needs

- Strong authentication and secure password handling
- Object-level authorization to prevent IDOR
- Request integrity protection via CSRF tokens
- Browser-side framing protection against clickjacking
- Secure defaults in CI/CD and dependency hygiene

## 5. Abuse Cases

1. User A modifies User B post by changing object ID in endpoint.
2. Victim browser submits forged request from attacker site.
3. Application loaded in attacker-controlled iframe for clickjacking.

## 6. Security Requirements

- Enforce ownership validation on every object read/write operation.
- Require CSRF token on all state-changing endpoints.
- Set anti-framing headers globally for all responses.
- Run SAST and dependency scanning on each push/PR.

## 7. Traceability to CLO

- CLO-5: Vulnerability analysis and mitigation was performed.
- CLO-6: Team-based secure software development workflow was implemented.

Update: Reviewed by ByteGuard team for PR evidence.
