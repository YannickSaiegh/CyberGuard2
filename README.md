# CyberGuard AI 🛡️🤖

Plataforma de Cibersegurança com Inteligência Artificial desenvolvida por uma equipa de 4 alunos do curso profissional de **Técnico de Desenvolvimento de Software**.

## 👥 Divisão da Equipa
- **Elemento 1:** Backend Flask, rotas e arquitetura da REST API (`app.py`, `config.py`).
- **Elemento 2:** Frontend UI/UX, design Superdesign, animações e gráficos (`templates/`, `static/`).
- **Elemento 3:** Motores de cibersegurança e integração com a API Google Gemini (`services/`).
- **Elemento 4:** Base de dados SQLite, testes, controlo de versões Git e documentação (`database/`, `README.md`).

## 🚀 Funcionalidades Principais
1. **Analisador de URLs:** Inspeção heurística de esquemas, IPs e ofuscação (0–100).
2. **Detetor de Phishing com IA:** Análise semântica de mensagens através da Google Gemini API.
3. **Verificador de Passwords:** Cálculo local de entropia sem armazenamento de credenciais.
4. **Assistente de Cibersegurança:** Chatbot interativo focado em educação defensiva.

## 🛠️ Instalação e Execução
```bash
git clone [https://github.com/teu-utilizador/CyberGuardAI.git](https://github.com/teu-utilizador/CyberGuardAI.git)
cd CyberGuardAI
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env
# Configura a tua GEMINI_API_KEY no .env
python app.py
