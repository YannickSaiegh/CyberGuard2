import re
from urllib.parse import urlparse


def analyze_url(raw_url: str) -> dict:
    """Motor heurístico de inspeção lexical e estrutural de URLs."""
    if not raw_url:
        return {"valid": False, "error": "URL vazio."}

    # Garante que o URL possui esquema
    if not raw_url.startswith(("http://", "https://")):
        normalized_url = "https://" + raw_url
    else:
        normalized_url = raw_url

    parsed = urlparse(normalized_url)
    domain = parsed.netloc.lower()
    scheme = parsed.scheme.lower()

    if not domain:
        return {"valid": False, "error": "Formato de domínio inválido."}

    score = 0
    indicators = []

    # 1. Verificação de protocolo HTTP vs HTTPS
    is_https = (scheme == "https")
    if not is_https:
        score += 35
        indicators.append("Utiliza protocolo HTTP inseguro (sem encriptação SSL/TLS).")
    else:
        indicators.append("Utiliza protocolo HTTPS encriptado.")

    # 2. Deteção de endereço IP direto no domínio
    ip_pattern = re.compile(r"^\d{1,3}(\.\d{1,3}){3}$")
    if ip_pattern.match(domain.split(":")[0]):
        score += 45
        indicators.append("O domínio é um endereço IP direto (prática comum em phishing e servidores de C2).")

    # 3. Presença do símbolo @ (ofuscação de URL)
    if "@" in parsed.netloc:
        score += 40
        indicators.append("Presença do carácter '@' no domínio, utilizado para ofuscar o destino real.")

    # 4. Comprimento excessivo do URL
    if len(normalized_url) > 90:
        score += 20
        indicators.append("URL com comprimento excessivo, frequentemente utilizado para ocultar parâmetros maliciosos.")

    # 5. Palavras-chave suspeitas de engenharia social
    suspicious_keywords = ["login", "verify", "update", "account", "secure", "bank", "signin", "confirm", "wallet"]
    found_keywords = [kw for kw in suspicious_keywords if kw in normalized_url.lower()]
    if found_keywords:
        score += 25 * len(found_keywords)
        indicators.append(f"Contém palavras-chave associadas a phishing: {', '.join(found_keywords)}.")

    # Limita a pontuação entre 0 e 100
    score = min(score, 100)

    if score >= 60:
        classification = "Risco Elevado"
        summary = "URL detetado com múltiplos indicadores estruturais suspeitos."
    elif score >= 30:
        classification = "Risco Médio"
        summary = "URL apresenta algumas características atípicas que requerem atenção."
    else:
        classification = "Risco Baixo"
        summary = "Estrutura do URL limpa e sem indicadores óbvios de risco."

    return {
        "valid": True,
        "normalized_url": normalized_url,
        "domain": domain,
        "scheme": scheme,
        "is_https": is_https,
        "risk_score": score,
        "classification": classification,
        "summary": summary,
        "indicators": indicators,
        "analysis_mode": "Heurística Estrutural e Lexical"
    }
