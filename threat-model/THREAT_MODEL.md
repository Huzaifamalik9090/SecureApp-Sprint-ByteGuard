Threat Model Report
ByteGuard Secure Blog Application
Course
CYC386 - Secure Software Design and Development (Spring 2026)
Team
ByteGuard
Instructor
Engr. Muhammad Ahmad Nawaz

1. System Overview
The ByteGuard Secure Blog is a Flask-based web application that allows authenticated users to create, edit, and delete their own posts. The application includes authentication, session handling, post management, and CI/CD security automation.

2. Data Flow Diagram (DFD) Components
The following components are included in the threat model:
* External User (authenticated/unauthenticated)
* Flask Web Application
* Authentication Module
* Post Management Service
* SQLite Database
* GitHub Actions CI/CD Pipeline

3. STRIDE Threat Analysis
ComponentSTRIDE CategoryExample ThreatMitigation ImplementedAuthentication ModuleSpoofingCredential stuffing / account abusePassword hashing, strong authentication controls (future: lockout/rate limiting)Post RoutesTamperingIDOR attack on edit/delete endpointsObject-level authorization checks on each protected objectForm Submission LayerRepudiationUser action cannot be tracedAction logging recommended (future enhancement)DatabaseInformation DisclosureUnauthorized access to another user’s postOwnership verification and least-privilege accessSession ManagementElevation of PrivilegeSession misuse / forged state-changing requestsSecure cookie settings + CSRF token validationBrowser RenderingClickjackingUI redress via malicious iframe embeddingX-Frame-Options: DENY + CSP frame-ancestors 'none'4. CVSS v3.1 Risk Assessment
VulnerabilityCVSS Base ScoreSeverityJustificationIDOR8.1HighAuthenticated attacker can modify or delete another user’s dataCSRF6.5MediumVictim can be forced to perform unintended actions in active sessionClickjacking4.3MediumUser interface can be manipulated through framing attacks
5. Attack Tree (Textual Representation)
Root Objective: Perform unauthorized data manipulation or user action abuse.
Branch 1: Unauthorized Object Access (IDOR)
1. Identify predictable object identifiers
2. Submit requests to protected edit/delete routes
3. Exploit missing ownership checks to alter other users’ data
Branch 2: Cross-Site Request Forgery (CSRF)
1. Create malicious external form/request
2. Trick authenticated victim into loading attacker content
3. Force unintended state-changing action
Branch 3: Clickjacking
1. Embed target application in hidden/overlay iframe
2. Deceive user through UI redress
3. Trigger unauthorized clicks/actions
6. Security Conclusions
The threat modeling and risk assessment process identified three priority risks aligned with OWASP Top 10 requirements for this sprint: IDOR, CSRF, and Clickjacking. ByteGuard implemented technical controls for each risk area and integrated automated security checks into CI/CD to improve assurance before release.

