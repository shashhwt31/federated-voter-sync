def normalize_string(value: str) -> str:
    return value.lower().strip()

def normalize_identity(name: str, dob: str) -> str:
    return f"{normalize_string(name)}|{dob}"
