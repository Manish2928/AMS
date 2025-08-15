from flask import Flask, render_template
from app.auth import auth
from app.student import student
from app.faculty import faculty
from app.admin import admin



def create_app():
    app = Flask(__name__)
    app.secret_key = "4d52ewmff33gg4577n"  # Needed for flash messages & forms

    app.register_blueprint(auth)
    app.register_blueprint(student)
    app.register_blueprint(faculty)
    app.register_blueprint(admin)


    # Import and register routes
    from app.routes.test_db import test_db
    app.register_blueprint(test_db)

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
