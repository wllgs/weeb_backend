import re

# Listes minimales FR (à étoffer selon ton contexte)
POSITIVE = {
    "merci", "super", "parfait", "top", "génial", "satisfait",
    "très bien", "nickel", "rapide", "excellent", "content", "heureux",
}
NEGATIVE = {
    "nul", "déçu", "insatisfait", "mécontent", "horrible", "problème",
    "lent", "bug", "pas content", "mauvais", "décevant",
}

def _normalize(text: str) -> str:
    text = text.lower()
    text = re.sub(r"[^\w\sàâäéèêëîïôöùûüç-]", " ", text)
    return re.sub(r"\s+", " ", text).strip()

def satisfaction_score(text: str) -> float:
    """
    Renvoie un score [0..1] naïf basé sur la présence de mots
    positifs/négatifs. À remplacer par un modèle ML entraîné si besoin.
    """
    t = _normalize(text)
    pos = sum(1 for w in POSITIVE if w in t)
    neg = sum(1 for w in NEGATIVE if w in t)
    total = pos + neg
    if total == 0:
        return 0.5  # neutre
    return max(0.0, min(1.0, (pos / total)))

def is_satisfied(text: str) -> bool:
    """Retourne True si score >= 0.6 (seuil ajustable)."""
    return satisfaction_score(text) >= 0.6
