from src.crypto.aes_crypto import generate_key
from src.key_manager import save_key, load_key
from src.vault import encrypt_and_store, decrypt_and_verify

def main():
    key = load_key()
    if not key:
        key = generate_key()
        save_key(key)

    filename = input("Enter file name to encrypt: ")

    with open(filename, "rb") as f:
        data = f.read()

    encrypted, file_hash = encrypt_and_store(data, key)

    with open(filename + ".enc", "wb") as f:
        f.write(encrypted)

    print("File encrypted successfully.")

    decrypted, verified = decrypt_and_verify(encrypted, file_hash, key)
    print("Integrity verified:", verified)

if __name__ == "__main__":
    main()
