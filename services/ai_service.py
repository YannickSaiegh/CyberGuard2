import os
import requests
from config import Config


def get_gemini_client():
    """Tenta carregar o SDK oficial do Google GenAI se disponível."""
    if not Config.is_ai_configured():
        return None
    try:
        from google import genai
        return genai.Client(api_key=Config.GEMINI_API_KEY)
    except Exception:
        return None


def ask_cyber_assistant(prompt: str) -> dict:
    """Assistente de Cibersegurança Ética e Defensiva."""
    system_instruction = (
        " És o assistente de cibersegurança do CyberGuard AI. "
        "O teu objetivo é exclusivamente educacional e defensivo. "
        "Explica conceitos técnicos, vulnerabilidades e formas de proteção de forma clara, "
        "rigorosa e acessível para estudantes. Recusa estritamente pedidos de ataques ofensivos ou ilegais."
    )

    if not Config.is_ai_configured():
        return {
            "reply": (
                "⚠️ A chave da API Gemini não está configurada no ficheiro `.env`. "
                "Para ativar o assistente inteligente, adiciona a tua chave `GEMINI_API_KEY=...` no ficheiro `.env`."
            ),
            "ai_used": False
        }

    # 1. Tenta usar o SDK oficial
    client = get_gemini_client()
    if client:
        try:
            full_prompt = f"{system_instruction}\n\nQuestão do Utilizador: {prompt}"
            response = client.models.generate_content(
                model=Config.GEMINI_MODEL,
                contents=full_prompt,
            )
            return {"reply": response.text, "ai_used": True}
        except Exception:
            pass

    # 2. Fallback para pedido direto REST API (compatível com cURL / endpoint Gemini)
    try:
        url = f"https://generativelanguage.googleapis.com/v1beta/models/{Config.GEMINI_MODEL}:generateContent?key={Config.GEMINI_API_KEY}"
        payload = {
            "contents": [{
                "parts": [{"text": f"{system_instruction}\n\n{prompt}"}]
            }]
        }
        headers = {"Content-Type": "application/json"}
        resp = requests.post(url, json=payload, headers=headers, timeout=10)
        if resp.status_code == 200:
            data = resp.json()
            candidates = data.get("candidates", [])
            if candidates:
                text_out = candidates[0].get("content", {}).get("parts", [{}])[0].get("text", "")
                if text_out:
                    return {"reply": text_out, "ai_used": True}
    except Exception:
        pass

    return {
        "reply": "Não foi possível estabelecer ligação com a API Gemini neste momento. Verifica a ligação à internet e a validade da chave.",
        "ai_used": False
    }


def analyze_phishing_with_ai(content: str, source_type: str) -> dict:
    """Analisa conteúdos de phishing utilizando o Gemini para gerar explicações detalhadas."""
    prompt = (
        f"Analisa o seguinte conteúdo do tipo '{source_type}' em busca de tentativas de phishing, "
        f"engenharia social, urgência artificial e falsificação de identidade:\n\n\"{content}\"\n\n"
        "Responde estritamente no seguinte formato:\n"
        "PONTUACAO: [número inteiro de 0 a 100]\n"
        "RESUMO: [uma frase com o veredito de risco]\n"
        "INDICADORES: [indicar 2 ou 3 sinais principais separados por vírgula]\n"
        "EXPLICACAO: [explicação detalhada e pedagógica em português sobre o perigo]"
    )

    ai_result = ask_cyber_assistant(prompt)
    raw_text = ai_result.get("reply", "")

    # Valores predefinidos por defeito caso o parsing falhe
    score = 75
    summary = "Possível tentativa de phishing detetada por IA."
    indicators = ["Linguagem de urgência", "Link suspeito embutido"]
    explanation = raw_text

    try:
        lines = raw_text.split("\n")
        for line in lines:
            if line.startswith("PONTUACAO:"):
                score = int("".join(filter(str.isdigit, line.split(":", 1)[1])))
            elif line.startswith("RESUMO:"):
                summary = line.split(":", 1)[1].strip()
            elif line.startswith("INDICADORES:"):
                indicators = [i.strip() for i in line.split(":", 1)[1].split(",")]
            elif line.startswith("EXPLICACAO:"):
                explanation = line.split(":", 1)[1].strip()
    except Exception:
        pass

    score = max(0, min(100, score))
    classification = "Risco Elevado" if score >= 60 else ("Risco Médio" if score >= 30 else "Risco Baixo")

    return {
        "risk_score": score,
        "classification": classification,
        "summary": summary,
        "indicators": indicators,
        "ai_explanation": explanation,
        "ai_used": ai_result.get("ai_used", False)
    }
