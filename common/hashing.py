import hashlib

def hash_value(value: str, salt: str) -> str:
    return hashlib.sha256(f"{value}{salt}".encode()).hexdigest()
