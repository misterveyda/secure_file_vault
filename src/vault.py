from src.crypto.aes_crypto import encrypt_file, decrypt_file
from src.crypto.hash_utils import hash_data

def encrypt_and_store(file_bytes, key):
    encrypted = encrypt_file(file_bytes, key)
    file_hash = hash_data(file_bytes)
    return encrypted, file_hash

def decrypt_and_verify(encrypted_bytes, original_hash, key):
    decrypted = decrypt_file(encrypted_bytes, key)
    return decrypted, hash_data(decrypted) == original_hash
