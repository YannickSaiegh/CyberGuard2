import math
import re


def evaluate_password_strength(password: str) -> dict:
    """Avalia a entropia e segurança da palavra-passe estritamente em memória."""
    length = len(password)
    has_lower = bool(re.search(r"[a-z]", password))
    has_upper = bool(re.search(r"[A-Z]", password))
    has_digits = bool(re.search(r"\d", password))
    has_symbols = bool(re.search(r"[^a-zA-Z0-9]", password))

    # Cálculo do espaço de caracteres (charset pool size)
    charset_size = 0
    if has_lower:
        charset_size += 26
    if has_upper:
        charset_size += 26
    if has_digits:
        charset_size += 10
    if has_symbols:
        charset_size += 32

    # Cálculo de Entropia em bits (H = L * log2(R))
    entropy_bits = round(length * math.log2(charset_size), 1) if charset_size > 0 and length > 0 else 0.0

    score = 0
    suggestions = []

    # Critérios de Pontuação
    if length >= 12:
        score += 35
    elif length >= 8:
        score += 20
        suggestions.append("Aumenta o comprimento para pelo menos 12 caracteres.")
    else:
        suggestions.append("Palavra-passe demasiado curta (mínimo recomendado: 12 caracteres).")

    if has_lower and has_upper:
        score += 20
    else:
        suggestions.append("Combina letras maiúsculas e minúsculas.")

    if has_digits:
        score += 20
    else:
        suggestions.append("Adiciona números para aumentar a diversidade.")

    if has_symbols:
        score += 25
    else:
        suggestions.append("Inclui símbolos especiais (ex: !, @, #, $).")

    score = min(score, 100)

    if score >= 80:
        strength_label = "Forte"
    elif score >= 50:
        strength_label = "Moderada"
    else:
        strength_label = "Fraca"

    return {
        "length": length,
        "has_lowercase": has_lower,
        "has_uppercase": has_upper,
        "has_digits": has_digits,
        "has_symbols": has_symbols,
        "entropy_bits": entropy_bits,
        "score": score,
        "strength_label": strength_label,
        "suggestions": suggestions if suggestions else ["Excelente palavra-passe! Mantém a confidencialidade."]
    }
