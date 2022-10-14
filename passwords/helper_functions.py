from cryptography.fernet import Fernet

def encrypt(key: bytes, message: bytes) -> bytes:
    return Fernet(key).encrypt(message)

def decrypt(key: bytes, token: bytes) -> bytes:
    return Fernet(key).decrypt(token)