🌟 Overview

CyberGuard AI is a state-of-the-art web application engineered to simulate enterprise-grade security operations. It combines static file malware analysis, hexadecimal packet inspection, SIEM log hunting, MITRE ATT&CK mapping, and OSINT reconnaissance into a single, high-performance, responsive interface with a sleek Red Noir aesthetic.

🚀 Key Modules & Features (26 Technical Tools)

🦠 Malware Analysis & Reverse Engineering

Drag & Drop Malware Sandbox (filescan): Calculates SHA-256 hashes (via Web Crypto API), inspects binary Magic Bytes (e.g., 4D 5A MZ headers), detects double extensions (.pdf.exe), and simulates 64 multi-engine antivirus checks.

Malware Payload Deobfuscator (deobfuscator): Decodes obfuscated PowerShell (-EncodedCommand), Base64, Hexadecimal, and String.fromCharCode scripts, automatically extracting C2 IP addresses, domains, and malicious commands.

YARA Rule Builder (yara): Generates formal YARA hunting signatures with custom hex patterns and suspicious API call strings for EDR deployment.

🔍 OSINT & Reconnaissance

Heuristic URL Analyzer (scanner): Passively inspects HTTPS/HTTP protocols, direct IPv4 hosts, @ symbol obfuscation, and high-risk TLDs (.xyz, .top).

QR Code Quishing Inspector (quishing): Decodes hidden payloads inside QR codes to detect malicious phishing redirects or rogue Wi-Fi (Evil Twin) configurations.

Network & Port Recon (ipscanner): Simulates geolocation, ISP identification, and open port checks (SSH, RDP).

DNS, WHOIS & Subdomain Mapping (osint-dns): Audits SPF/DMARC alignment, SSL certificates, and DNS records.

Sherlock Username Tracker (osint-user): Searches digital footprints across 8 major public social networks and developer platforms.

Google Dorks GHDB Generator (dorks): Generates advanced search operators (site: target.pt ext:env) to audit public exposure of configuration files and database backups.

EXIF Metadata Inspector & Scrubber (exif): Extracts and strips sensitive GPS coordinates and device model metadata from images for privacy protection.

Dark Web Leak Checker (breach): Scans email addresses against simulated breach databases.

🛡️ SOC, SIEM & Threat Intelligence

Email Forensics & Anti-Spoofing (email-headers): Detects Display Name Spoofing, header mismatches between From and Return-Path, and SPF/DKIM/DMARC failures.

SIEM Log Hunter & Sigma Rule Builder (siem-sigma): Tests Regular Expressions against Linux authentication logs and web server access logs to generate exportable Sigma (.yml) detection rules.

MITRE ATT&CK® Tactical Mapper (mitre-matrix): Interactive adversary TTP matrix providing EDR queries and Blue Team mitigations for techniques like Initial Access (T1566) and Credential Dumping (T1003).

SSL/TLS & Cipher Suite Auditor (ssl-inspector): Evaluates X.509 certificate validity, TLS 1.3 support, and Perfect Forward Secrecy.

IPv4 CIDR Subnet Calculator (cidr-calc): Bitwise subnetting, wildcard masks, broadcast addresses, and VLAN host capacity calculations.

Packet Hex Dump Inspector (pcap): Low-level packet analyzer showing offsets, hexadecimal payloads, and ASCII translations for cleartext HTTP credentials or DNS tunneling.

CVSS v3.1 Severity Calculator (cvss): Computes official vulnerability scores (0.0 to 10.0) based on attack vectors and the CIA triad.

OWASP Security Headers & JWT Auditor (headers, jwt): Audits HSTS/CSP headers and decodes JSON Web Tokens (including alg: none vulnerability detection).

Firewall Rule Generator (firewall): Generates ufw/iptables and Nginx/Apache configuration rules to block malicious IPs and protect sensitive endpoints (.env, .git).

🔐 Cryptography, Training & Management

SQL Injection & XSS Sandboxes (sqli, xss): Demonstrates OWASP Top 10 vulnerabilities and compares vulnerable string concatenation with parameterized queries and DOM sanitization.

Password Entropy & Security Checker (password): Zero-storage entropy calculations and secure password generator.

Cryptography Lab (crypto): Base64, Caesar Cipher, and Hex encoders/decoders.

SQLite Scan History & CSV Export (history): Complete searchable audit log with CSV export capabilities.

Gemini AI Security Assistant (assistant): Context-aware defensive AI helper.

Verified Feedback & Bug Reporting (feedback): Secure ticketing system tied directly to user sessions, routed to cyberguard@proton.me.

🔐 Authentication & RBAC (Role-Based Access Control)

Direct SQLite Authentication (SHA-256): Fast native login and account creation without email OTP overhead.

Multilingual Profanity Filter: Built-in blacklisting filter that screens usernames and emails against offensive terminology across multiple languages (PT, EN, ES, FR, DE, IT) to prevent improper inputs.

Privilege Levels:

Administrator Accounts: Full access to the SQLite users table, Live Threat Feed, and advanced engineering/OSINT modules. (Default Admin: admin@cyberguard.pt | Password: nigga333larp)

Standard Users: Access to core analysis tools and personal security features.

🚀 Quick Start & Installation

Clone the repository:

git clone https://github.com/your-username/cyberguard-ai.git
cd cyberguard-ai


Run locally:
The project is built as a robust single-file architecture (index.html) utilizing CDN-delivered dependencies (Tailwind CSS, Chart.js, Iconify). You can open it directly in any modern web browser or serve it via a local HTTP server:

python3 -m http.server 8080


Access the platform:
Open your browser at http://localhost:8080.

🛡️ License

Distributed under the MIT License. See LICENSE for more information.
