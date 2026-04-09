# FINAL REPORT - BYTEGUARD SECURE BLOG

## Page 1 - Title Page

COMSATS University Islamabad  
Department of Computer Science  
CYC386 - Secure Software Design and Development (Spring 2026)  
Midterm Lab Exam - 48-Hour DevSecOps Security Engineering Sprint  

Final Project Report  
ByteGuard Secure Blog Application  

Submitted by Team ByteGuard  
Member 1: [Name - Reg No]  
Member 2: [Name - Reg No]  
Member 3: [Name - Reg No]  
Member 4: [Name - Reg No, if applicable]  

Submitted to:  
Engr. Muhammad Ahmad Nawaz  
Instructor, CYC386  
Submission Date: [Insert Date]

## Page 2 - Declaration and Acknowledgment

### Declaration of Original Work

We hereby declare that this project report and implementation have been completed by Team ByteGuard as part of the CYC386 Midterm Lab Exam. The work presented in this report is original and prepared by the team according to the provided exam guidelines. Any external resources, frameworks, and references used in this project have been properly acknowledged. We understand that plagiarism and academic dishonesty are subject to disciplinary action under university policy.

### Acknowledgment

We would like to thank our instructor, Engr. Muhammad Ahmad Nawaz, for designing this industry-oriented DevSecOps sprint and for providing practical guidance throughout the course. We also acknowledge COMSATS University Islamabad for offering an applied security engineering environment where students can practice secure development, threat analysis, and security testing. This sprint helped us understand real-world secure software delivery under strict deadlines and team collaboration constraints.

### Team Signatures

Member 1: ____________________  
Member 2: ____________________  
Member 3: ____________________  
Member 4: ____________________

## Page 3 - Abstract and Keywords

### Abstract

This report presents the end-to-end execution of a 48-hour DevSecOps Security Engineering Sprint conducted by Team ByteGuard for CYC386 Secure Software Design and Development. The selected project is a Flask-based secure blog platform where users can register, authenticate, and perform post management operations. The sprint objective was to transform a baseline application into an attack-resistant software system by integrating secure design, vulnerability mitigation, and automated security assurance processes.

The team performed Protection Needs Elicitation (PNE) to identify critical assets, threat actors, and security requirements. Threat modeling was carried out using STRIDE with Data Flow Diagram (DFD) analysis, followed by CVSS v3.1 risk scoring to prioritize vulnerabilities. Three mandatory vulnerabilities from OWASP Top 10 themes were addressed: Insecure Direct Object Reference (IDOR), Cross-Site Request Forgery (CSRF), and Clickjacking. For IDOR mitigation, object-level authorization checks were enforced across sensitive routes. For CSRF mitigation, global anti-CSRF protection and secure form token validation were implemented. For Clickjacking prevention, anti-framing HTTP security headers were added at middleware level.

A CI/CD pipeline was developed in GitHub Actions to automate build, test, static security analysis, dependency vulnerability audit, and baseline dynamic security testing. The pipeline integrates pytest, Bandit, pip-audit, CodeQL, and OWASP ZAP baseline scanning. Security validation shows that exploitability was reduced significantly in post-mitigation tests. This sprint demonstrates practical alignment with secure SDLC principles and CLO requirements for vulnerability analysis and team-based secure development.

### Keywords

DevSecOps, Secure SDLC, STRIDE, CVSS v3.1, IDOR, CSRF, Clickjacking, Flask Security, CI/CD, SAST, DAST, GitHub Actions, OWASP

## Page 4 - Table of Contents

1. Introduction  
2. Project Scope and Objectives  
3. Methodology  
4. Protection Needs Elicitation (PNE)  
5. System Architecture and Data Flow  
6. STRIDE Threat Modeling  
7. CVSS Risk Assessment  
8. Vulnerability Analysis and Mitigation  
9. Secure Implementation Details  
10. DevSecOps CI/CD Pipeline  
11. Security Testing and Results  
12. Team Workflow and PR Strategy  
13. CLO Mapping and Learning Outcomes  
14. Challenges and Lessons Learned  
15. Conclusion and Future Enhancements  
16. References  
17. Appendices

## Page 5 - Introduction

Software security has become a foundational requirement in modern application development due to increased attack frequency, public vulnerability disclosure, and strict compliance demands. Traditional development methods that defer security checks until after coding are no longer sufficient, particularly in fast-paced deployment environments. DevSecOps addresses this issue by embedding security controls into every phase of software delivery, from planning and coding to testing and deployment.

The CYC386 midterm sprint was structured to simulate a real-world security engineering engagement. Team ByteGuard was tasked to harden an application under strict time constraints and provide evidence-based results. The selected implementation, ByteGuard Secure Blog, is a web application developed in Flask that includes user authentication and post management capabilities.

## Page 6 - Project Scope and Objectives

### 2.1 Scope

- User registration and login  
- Session-based authentication  
- Create/read/update/delete operations for posts  
- Server-side validation and secure response behavior  
- GitHub-based source control and automated CI security checks

### 2.2 Objectives

1. Perform PNE to identify system assets, trust boundaries, threat actors, and security requirements.  
2. Conduct threat modeling through DFD and STRIDE to systematically identify vulnerabilities.  
3. Assess identified risks using CVSS v3.1 and prioritize remediation under timeline constraints.  
4. Implement robust mitigations for IDOR, CSRF, and Clickjacking vulnerabilities.  
5. Integrate CI/CD automation with security checks (SAST, dependency audit, DAST).  
6. Produce professional documentation and evidence suitable for final submission and viva.

## Page 7 - Methodology

Team ByteGuard followed a practical multi-phase approach aligned with secure SDLC and DevSecOps practices:

- Phase 1: Requirement and Protection Analysis  
- Phase 2: Threat Modeling and Risk Prioritization  
- Phase 3: Secure Implementation  
- Phase 4: Automation and Testing  
- Phase 5: Documentation and Delivery

## Page 8 - Protection Needs Elicitation

### 4.1 Critical Assets

1. User credentials (password hashes, login data)  
2. Session cookies and authenticated state  
3. User-owned posts and content integrity  
4. Source code and repository history  
5. CI/CD configurations and scan outputs

### 4.2 Threat Actors

- External unauthenticated attacker probing public endpoints  
- Authenticated malicious user attempting privilege escalation  
- Opportunistic bot/scanner targeting common web flaws  
- Insider misuse through improper access behavior

## Page 9 - System Architecture and DFD Level 0

ByteGuard Secure Blog follows a monolithic Flask architecture with modular routes and middleware controls.  
Insert Figure: DFD Level 0 JPG.

## Page 10 - DFD Level 1 and Trust Boundaries

Insert Figure: DFD Level 1 JPG.

Trust boundaries:

- Browser -> Web App  
- Web App -> Database  
- Repository -> CI Runner

## Page 11 - STRIDE Threat Modeling

Insert Table 2 (STRIDE Matrix).

Key findings:

- F1: IDOR risk due to missing object-level checks  
- F2: CSRF risk due to missing anti-CSRF validation  
- F3: Clickjacking risk due to missing anti-framing policy

## Page 12 - CVSS Risk Assessment

Insert Table 3.

- IDOR: 8.1 (High)  
- CSRF: 6.5 (Medium)  
- Clickjacking: 4.3 (Medium)

## Page 13 - Attack Tree and Exploitation Paths

Insert Figure: Attack Tree JPG.

Root Goal: Unauthorized data/action manipulation.

## Page 14 - Vulnerability 1: IDOR

Issue: Non-owner resource access by manipulated object ID.  
Fix: Object-level owner check helper with HTTP 403 on unauthorized access.  
Evidence: Unauthorized route + 403 screenshot.

## Page 15 - Vulnerability 2: CSRF

Issue: Forged state-changing requests.  
Fix: Flask-WTF CSRF protection + secure cookies.  
Evidence: CSRF token in request + rejection behavior screenshot.

## Page 16 - Vulnerability 3: Clickjacking

Issue: Potential iframe-based UI redress.  
Fix: `X-Frame-Options: DENY` and `Content-Security-Policy: frame-ancestors 'none'`.  
Evidence: Response headers screenshot.

## Page 17 - Secure Implementation and Code Quality

Core stack:

- Flask
- Flask-Login
- Flask-WTF
- SQLAlchemy

Implementation highlights:

- Centralized authorization guard
- CSRF on all state-changing forms
- Header hardening middleware
- Validation and cleaner route structure

## Page 18 - DevSecOps Pipeline and Testing

Pipeline stages:

1. Build and dependency installation
2. Pytest execution
3. Bandit SAST
4. pip-audit
5. CodeQL
6. OWASP ZAP baseline

Insert Figure: GitHub Actions CI/CD screenshot.

## Page 19 - Team Workflow, CLO Mapping, Challenges

Branching model:

- feature branches -> develop -> main

Merged PRs provide collaboration evidence.  
CLO-5 and CLO-6 were met through mitigation, testing, and team-based secure delivery.

## Page 20 - Conclusion, Future Work, References

Team ByteGuard successfully completed the 48-hour DevSecOps sprint and delivered an attack-resistant application with mandatory vulnerability mitigations and automated pipeline validation.

### Future Enhancements

- RBAC and fine-grained authorization
- Rate-limiting and anti-bruteforce controls
- Centralized logging and monitoring
- Authenticated DAST profiles
- Container hardening and policy controls

### References

1. OWASP Top 10  
2. FIRST CVSS v3.1  
3. GitHub Actions Docs  
4. OWASP ZAP Docs  
5. Flask Security Docs  
6. SQLAlchemy Best Practices

## Table 1 - Protection Needs and Security Requirements

| ID | Asset / Area | Threat Concern | Security Requirement | Implemented Control |
|---|---|---|---|---|
| R1 | User Accounts | Unauthorized account usage | Secure authentication handling | Password hashing + login checks |
| R2 | Post Objects | IDOR / object tampering | Object-level authorization on each object access | Owner-check guard in post routes |
| R3 | Form Requests | Cross-site forged actions | CSRF protection for state-changing requests | Flask-WTF CSRF tokens |
| R4 | Browser Rendering | Clickjacking / UI redress | Prevent framing by untrusted origins | XFO + CSP frame-ancestors |
| R5 | Sessions | Session misuse | Harden session cookie behavior | HttpOnly + SameSite policy |
| R6 | Source & Delivery | Security regressions in release | Security checks on each push/PR | GitHub Actions security pipeline |

## Table 2 - STRIDE Analysis Matrix

| Component | STRIDE Category | Example Threat | Impact | Mitigation |
|---|---|---|---|---|
| Authentication Module | Spoofing | Credential abuse attempts | Account compromise risk | Password hashing, secure auth flow |
| Post Routes | Tampering | IDOR via manipulated post ID | Unauthorized data modification | Owner authorization checks |
| Action Logging Layer | Repudiation | User denies critical action | Forensic gaps | Logging enhancement planned |
| Database Access | Information Disclosure | Unauthorized data read | Privacy breach | Owner-bound object access |
| Session Handling | Elevation of Privilege | Forged authenticated actions | Unauthorized state change | CSRF token + secure cookies |
| Browser Interface | Clickjacking | Framed UI deception | Unintended user actions | Anti-framing headers |

## Table 3 - CVSS v3.1 Risk Assessment

| Vulnerability | CVSS Base Score | Severity | Attack Vector Summary | Priority |
|---|---:|---|---|---|
| IDOR | 8.1 | High | Authenticated attacker manipulates object identifier | P1 |
| CSRF | 6.5 | Medium | Victim coerced into forged request submission | P2 |
| Clickjacking | 4.3 | Medium | UI redress through malicious iframe | P3 |

## Table 4 - Before/After Mitigation Comparison

| Vulnerability | Before Mitigation | After Mitigation | Verification Result |
|---|---|---|---|
| IDOR | Non-owner could target object endpoints by ID | Non-owner blocked with HTTP 403 | Pass |
| CSRF | Forged request possibility on state-changing forms | Missing/invalid CSRF token rejected | Pass |
| Clickjacking | No anti-framing restrictions in responses | XFO + CSP frame-ancestors enforced | Pass |
| Pipeline Security | Manual checks only | Automated checks per push/PR | Pass |

## Table 5 - Security Toolchain Summary

| Tool / Stage | Category | Purpose | Output |
|---|---|---|---|
| pytest | Testing | Validate application behavior and controls | Unit test pass/fail |
| Bandit | SAST | Detect common Python security issues | Static scan report |
| pip-audit | Dependency Security | Detect known vulnerable packages | Vulnerability list/status |
| CodeQL | Advanced SAST | Semantic analysis for security patterns | Security alerts/report |
| OWASP ZAP Baseline | DAST | Baseline dynamic web security scan | Runtime scan findings |
| GitHub Actions | CI/CD Orchestration | Automate quality + security gates | Workflow status |
