import os
from src.crypto.aes_crypto import generate_key

KEY_FILE = "aes.key"

def save_key(key):
    with open(KEY_FILE, "wb") as f:
        f.write(key)

def load_key():
    if not os.path.exists(KEY_FILE):
        return None
    with open(KEY_FILE, "rb") as f:
        return f.read()
