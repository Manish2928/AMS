from functools import wraps
from flask import session, redirect, url_for, flash

def login_required(view):
    @wraps(view)
    def wrapped(*args, **kwargs):
        if not session.get("user_id"):
            flash("Please log in first.", "warning")
            return redirect(url_for("auth.login"))
        return view(*args, **kwargs)
    return wrapped

def roles_required(*roles):
    roles_lc = {r.lower() for r in roles}
    def wrapper(f):
        @wraps(f)
        def decorated(*args, **kwargs):
            role = (session.get("role") or session.get("user_type") or "").lower()
            if role not in roles_lc:
                flash("You do not have access to this page.", "danger")
                return redirect(url_for("auth.login"))
            return f(*args, **kwargs)
        return decorated
    return wrapper

