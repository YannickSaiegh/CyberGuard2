CyberGuard AI — Plataforma SOC, OSINT & Cibersegurança

CyberGuard AI é uma plataforma avançada de cibersegurança e operações de SOC (Security Operations Center), desenvolvida como Projeto Técnico de Desenvolvimento de Software (TDS). A aplicação integra um ecossistema completo de ferramentas de análise forense, inteligência de ameaças (Threat Intel), auditoria de vulnerabilidades e testes defensivos.

🚀 Principais Módulos & Ferramentas (v2.4.1)

Malware Sandbox & Multi-Engine (filescan): Inspeção estática de ficheiros, cálculo de Hash SHA-256 (via Web Crypto API), leitura de Magic Bytes hexadecimais, deteção de dupla extensão (.pdf.exe) e simulação de 64 motores antivírus.

Desofuscador de Malware & Extrator de IOCs (deobfuscator): Descodifica payloads PowerShell -enc, Base64, Hexadecimal e String.fromCharCode, extraindo automaticamente IPs C2, URLs e comandos suspeitos.

Analisador de Cabeçalhos de Email & Anti-Spoofing (email-headers): Verifica o alinhamento entre From e Return-Path, deteta Display Name Spoofing e audita políticas SPF, DKIM e DMARC.

Analisador Heurístico de URLs (scanner): Inspeção passiva de protocolos HTTPS/HTTP, endereços IPv4 diretos, ofuscação com @ e TLDs de risco (.xyz, .top).

Detetor de Phishing com IA Gemini (phishing): Analisa mensagens SMS, WhatsApp e emails em busca de gatilhos de engenharia social e pânico artificial.

Inspetor de QR Codes / Anti-Quishing (quishing): Descodifica payloads maliciosos em códigos QR e identifica redes Wi-Fi Rogue (Evil Twin).

SIEM & Gerador de Regras Sigma (siem-sigma): Caça a ameaças em logs Linux/Web através de expressões regulares e exporta regras Sigma (.yml).

Matriz Tática MITRE ATT&CK® (mitre-matrix): Mapeamento de TTPs adversárias (Initial Access, Execution, Credential Dumping, Exfiltration), queries EDR e mitigações SOC.

Auditor SSL/TLS & Cipher Suites (ssl-inspector): Avalia certificados X.509, suporte a TLS 1.3 e Perfect Forward Secrecy.

Calculadora de Sub-redes CIDR (cidr-calc): Cálculo bitwise IPv4, máscara de sub-rede, broadcast e segmentação de VLANs.

Scanner de IP & Portas (ipscanner): Geolocalização, ISP e portas expostas (SSH, RDP).

Reconhecimento DNS, WHOIS & Subdomínios (osint-dns): Mapeamento SPF/DMARC e registos de domínios.

Rastreador de Username - Sherlock OSINT (osint-user): Pesquisa de pegada digital em 8 redes sociais e plataformas públicas.

Gerador de Google Dorks - GHDB (dorks): Operadores de pesquisa avançada para auditar exposição de ficheiros .env, .sql e diretórios expostos.

Inspetor & Limpador de Metadados EXIF (exif): Extração e remoção de coordenadas GPS e dados de câmara em imagens.

Verificador de Fugas de Dados Dark Web (breach): Pesquisa de credenciais comprometidas em bases de dados de violação.

Calculadora CVSS v3.1 (cvss): Classificação oficial (0.0 a 10.0) de vulnerabilidades baseada na Tríade CIA.

Inspetor OWASP Security Headers & JWT (headers, jwt): Auditoria de cabeçalhos HSTS/CSP e descodificação de tokens JWT (incluindo deteção da vulnerabilidade alg: none).

Gerador de Regras de Firewall UFW / Nginx (firewall): Bloqueio de IPs atacantes e hardening de servidores web.

Sandboxes de Injeção SQL & XSS (sqli, xss): Demonstração prática de vulnerabilidades OWASP Top 10 e respetiva mitigação (consultas parametrizadas e sanitização DOM).

🔐 Controlo de Acessos & Segurança

Autenticação SQLite Direta (SHA-256): Sem necessidade de 2FA por email. Registo e início de sessão imediatos.

Filtro Multilíngue de Linguagem Imprópria: O sistema valida automaticamente nomes de utilizador e emails contra uma lista negra exaustiva de termos ofensivos em várias línguas (PT, EN, ES, FR, DE, IT), rejeitando inputs inválidos.

Controlo de Acesso Baseado em Funções (RBAC):

Contas de Administrador (como admin@cyberguard.pt, com a palavra-passe nigga333larp) têm acesso total ao painel SQLite de utilizadores, Live Threat Feed e módulos avançados de engenharia/OSINT.

Contas de Utilizador Padrão têm acesso às ferramentas de análise e proteção pessoal.

🛠️ Como Executar o Projeto

Certifica-te de que tens um browser moderno (Chrome, Firefox, Edge, Safari) com suporte a HTML5, Tailwind CSS e Web Crypto API.

Faz o download ou clona o repositório contendo o ficheiro único index.html.

Abre o ficheiro index.html diretamente no teu browser ou serve-o através de um servidor web local (por exemplo, usando Python):

python3 -m http.server 8080


Acede a http://localhost:8080 para utilizar a plataforma.
