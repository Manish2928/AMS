from flask import Flask, render_template
from config import Config
from .extensions import csrf

def create_app():
    app = Flask(__name__, static_folder="static", template_folder="templates")
    app.config.from_object(Config)

    # Initialize extensions
    csrf.init_app(app)

    # --- Auth ---
    try:
        from app.auth import auth
        app.register_blueprint(auth, url_prefix="/auth")
    except Exception as e:
        print(f"[Warning] Auth blueprint not loaded: {e}")

    # --- Student ---
    try:
        from app.student import student
        app.register_blueprint(student, url_prefix="/student")
    except Exception as e:
        print(f"[Warning] Student blueprint not loaded: {e}")

    # --- Faculty ---
    try:
        from app.faculty import faculty
        app.register_blueprint(faculty, url_prefix="/faculty")
    except Exception as e:
        print(f"[Warning] Faculty blueprint not loaded: {e}")

    # --- Admin ---
    try:
        from app.admin import admin
        app.register_blueprint(admin, url_prefix="/admin")
    except Exception as e:
        print(f"[Warning] Admin blueprint not loaded: {e}")

    # --- Test DB Blueprint ---
    try:
        from app.routes.test_db import test
        app.register_blueprint(test)
    except Exception as e:
        print(f"[Warning] Test DB blueprint not loaded: {e}")

    # --- Main Routes ---
    @app.route("/")
    def home():
        return render_template("home.html")

    @app.route("/about")
    def about():
        return render_template("about.html")

    @app.route("/contact")
    def contact():
        return render_template("contact.html")

    @app.route("/base")
    def base():
        return render_template("base.html")

    return app
