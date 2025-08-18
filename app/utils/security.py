from werkzeug.security import generate_password_hash, check_password_hash
import hashlib

def hash_password(password: str) -> str:
    return generate_password_hash(password, method='pbkdf2:sha256')

def verify_password(password: str, password_hash: str) -> bool:
    try:
        return check_password_hash(password_hash, password)
    except (ValueError, TypeError) as e:
        # Handle corrupted or unsupported hash formats
        print(f"Password hash verification error: {e}")
        return False

def create_legacy_hash(password: str) -> str:
    """Create a simple hash for testing purposes"""
    return hashlib.sha256(password.encode()).hexdigest()

def verify_legacy_hash(password: str, password_hash: str) -> bool:
    """Verify legacy hash format"""
    try:
        return create_legacy_hash(password) == password_hash
    except:
        return False
