import os

def handle_x_webhook(payload_or_text):
    # Accept either dict or raw text
    text = payload_or_text if isinstance(payload_or_text, str) else payload_or_text.get("text", "")
    # WARNING: in production replace with OAuth1.0a or OAuth2 provider code
    # For now just print
    print("[X WEBHOOK] Posting to X/Twitter: ", text[:140])
    return True
