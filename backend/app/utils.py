import chardet

def detect_encoding(content: bytes) -> str:
    """
    Detects the text encoding of uploaded file content.
    Returns a safe fallback ('utf-8') if detection fails.
    """
    try:
        result = chardet.detect(content)
        encoding = result.get("encoding") or "utf-8"
        # Normalize common variants (e.g., 'utf_8' → 'utf-8')
        encoding = encoding.lower().replace("_", "-")
        return encoding
    except Exception:
        return "utf-8"
