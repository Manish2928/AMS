import secrets, datetime
from app.db_queries.admin_queries import set_password_reset_token, clear_reset_token, update_user_password
from app.utils.security import hash_password

def generate_reset_token(user_id: int, minutes_valid: int = 30) -> str:
    token = secrets.token_urlsafe(32)
    expiry = datetime.datetime.utcnow() + datetime.timedelta(minutes=minutes_valid)
    set_password_reset_token(user_id, token, expiry)
    return token

def consume_reset_token(user_id: int, new_password: str):
    new_hash = hash_password(new_password)
    ok = update_user_password(user_id, new_hash)
    if ok:
        clear_reset_token(user_id)
    return ok

# Stub to “send” email — integrate an email provider later
def send_reset_email(to_email: str, token: str):
    print(f"[DEV] Password reset link for {to_email}: /auth/reset-confirm?token={token}")
     # For frontend EmailJS: just return the link
    return f"http://127.0.0.1:5000/auth/reset-confirm?token={token}"