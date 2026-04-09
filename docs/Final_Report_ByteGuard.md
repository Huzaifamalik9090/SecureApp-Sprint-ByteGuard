# Final Report - ByteGuard Secure Blog

## Abstract

This report documents Team ByteGuard's 48-hour DevSecOps sprint for CYC386. The objective was to secure a Flask-based web application by applying protection needs elicitation, STRIDE threat modeling, CVSS risk scoring, secure coding, and automated security checks in CI/CD. The team implemented and validated fixes for three mandatory vulnerabilities: IDOR, CSRF, and Clickjacking. Security automation was integrated using GitHub Actions with testing and scanning stages, and release-readiness evidence was collected through pull request traceability and pipeline outcomes. The result is an attack-resistant application with reproducible security controls and submission-ready engineering documentation aligned with CLO-5 and CLO-6.

## 1. Introduction

Software applications are continuously exposed to threats that target weak authorization, unsafe request handling, and client-side trust assumptions. In fast development environments, security cannot be treated as a final checkpoint. DevSecOps addresses this issue by integrating security requirements and controls throughout planning, coding, testing, and delivery.

The CYC386 sprint was designed to simulate a real software security engagement. Team ByteGuard selected a Flask web application and transformed it into a more secure release candidate under strict time constraints. This report presents the project scope, architecture, threat model, risk analysis, mitigation strategy, and verification evidence.

## 2. Project Scope and Objectives

### 2.1 Scope

The project scope included:

- User registration and login.
- Session-based authentication.
- Post create/read/update/delete operations.
- Security control implementation for IDOR, CSRF, and Clickjacking.
- Automated CI/CD quality and security checks.
- Documentation and evidence artifacts for submission and viva.

### 2.2 Objectives

- Perform PNE to define assets, threats, and security requirements.
- Conduct STRIDE threat modeling with DFDs and attack tree.
- Score risks using CVSS v3.1 for remediation priority.
- Implement mandatory vulnerability fixes.
- Integrate SAST/DAST-enabled CI/CD.
- Produce professional final report and demo-ready evidence.

## 3. Methodology

Team ByteGuard followed a phase-based secure SDLC flow:

1. Protection needs elicitation and planning.
2. Threat modeling and risk scoring.
3. Secure implementation.
4. CI/CD and automated testing.
5. Evidence collection and reporting.

The process emphasized traceability between requirements, vulnerabilities, controls, and validation outcomes.

## 4. Protection Needs Elicitation (PNE)

### 4.1 Assets

- Credentials and password hashes.
- Session state and cookies.
- User-owned posts.
- Source code and CI workflow.
- Repository integrity and branch history.

### 4.2 Threat Actors

- External unauthenticated attackers.
- Authenticated malicious users.
- Automated scanners and opportunistic bots.

### 4.3 Protection Requirements

- Strict object-level authorization.
- Anti-CSRF token validation for state-changing actions.
- Anti-clickjacking response headers.
- Secure session cookie settings.
- Security checks integrated in CI pipeline.

## 5. System Architecture and Data Flow

### 5.1 Components

- External user/browser.
- Flask web application.
- Authentication module.
- Post service.
- SQLite database.
- GitHub Actions pipeline.

### 5.2 Trust Boundaries

- Browser to server boundary.
- Server to database boundary.
- Repository to CI runner boundary.

These boundaries were used to prioritize validation controls and route-level security checks.

## 6. STRIDE Threat Modeling

### 6.1 Findings Summary

- **Spoofing:** credential abuse attempts.
- **Tampering:** IDOR on object endpoints.
- **Repudiation:** limited logging trace depth.
- **Information disclosure:** cross-user data exposure risk.
- **Elevation of privilege:** forged authenticated actions.
- **UI manipulation:** clickjacking via malicious framing.

### 6.2 Threat Mitigation Mapping

- Auth hardening with hashed passwords.
- Owner checks for object access.
- CSRF middleware and tokenized forms.
- Security headers for anti-framing.

## 7. CVSS v3.1 Risk Assessment

| Vulnerability | CVSS Score | Severity | Priority |
|---|---:|---|---|
| IDOR | 8.1 | High | P1 |
| CSRF | 6.5 | Medium | P2 |
| Clickjacking | 4.3 | Medium | P3 |

IDOR was prioritized first due to direct unauthorized data modification risk.

## 8. Vulnerability Analysis and Fixes

### 8.1 IDOR

**Issue:** Resource identifiers could be targeted by non-owners.  
**Fix:** Centralized object ownership check with `403 Forbidden` on unauthorized access.  
**Outcome:** Non-owner edit/delete attempts blocked.

### 8.2 CSRF

**Issue:** State-changing actions vulnerable to forged requests.  
**Fix:** Global CSRF protection using Flask-WTF and tokenized forms; SameSite cookie policy.  
**Outcome:** Invalid/missing token requests rejected.

### 8.3 Clickjacking

**Issue:** Potential iframe-based UI redress attack path.  
**Fix:** `X-Frame-Options: DENY` and CSP `frame-ancestors 'none'`.  
**Outcome:** Framing by unauthorized origins prevented.

## 9. Secure Implementation Details

### 9.1 Code-Level Controls

- Object-level authorization helper for post routes.
- CSRF tokens in login/register/create/edit/delete/logout forms.
- Global response hardening middleware for headers.
- Input validation in forms.

### 9.2 Secure Defaults

- Session cookie hardening flags configured.
- Security checks applied server-side, not only UI-level hiding.

## 10. DevSecOps CI/CD Pipeline

### 10.1 Pipeline Stages

- Build and dependency install.
- Unit test execution with pytest.
- SAST with Bandit.
- Dependency audit with pip-audit.
- CodeQL analysis.
- DAST baseline with OWASP ZAP.

### 10.2 Workflow Benefits

- Continuous quality/security feedback.
- Faster detection of regressions.
- Documented proof of security operations.

## 11. Testing and Results

### 11.1 Manual Security Validation

- IDOR attack path returns HTTP 403.
- CSRF-protected actions require valid token.
- Clickjacking headers visible in response metadata.

### 11.2 Automated Validation

- Test suite passes in local and CI execution.
- Security scans integrated in pipeline.
- PR merge history validates collaborative engineering workflow.

## 12. Branching and Collaboration

Branches used:

- `main`
- `develop`
- `feature/pne-threat-model`
- `feature/secure-implementation`
- `feature/ci-security-testing`
- `feature/docs-final-submission`

Feature-specific pull requests were merged into `develop`, then integrated into `main`. This provided clear change traceability and review alignment.

## 13. Mapping to CLOs and GAs

### CLO-5 (Lab)

Achieved through vulnerability analysis, risk prioritization, mitigation implementation, and security validation.

### CLO-6 (Lab)

Achieved through team-based secure development workflow, branching strategy, PR-based integration, and CI/CD automation.

## 14. Challenges and Lessons Learned

### Challenges

- Tight 48-hour delivery window.
- Balancing implementation speed and documentation quality.
- Handling CI failures from external tooling dependencies.

### Lessons Learned

- Threat modeling early reduces rework.
- Server-side authorization must be explicit on each sensitive object path.
- CI/CD security automation improves confidence and repeatability.

## 15. Conclusion

Team ByteGuard completed a practical DevSecOps sprint aligned with course outcomes and industry expectations. The final application demonstrates hardened controls for IDOR, CSRF, and Clickjacking, supported by CI/CD-driven validation and strong documentation. The resulting process and deliverables are suitable for security review, viva demonstration, and resume-level project experience.

## 16. Future Enhancements

- Role-based access control for admin/moderator scenarios.
- Stronger auth controls (rate limiting, lockout policy).
- Centralized audit logging and alerting.
- Extended authenticated DAST profiles.
- Production deployment hardening with container policies.

## 17. References

1. OWASP Foundation, OWASP Top 10.
2. FIRST, CVSS v3.1 Specification.
3. GitHub Docs, GitHub Actions.
4. OWASP ZAP Baseline Scan Documentation.
5. Flask Security Documentation.
