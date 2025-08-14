from flask import render_template, redirect, url_for, request, flash
from . import auth
from datetime import datetime

@auth.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # TODO: Add authentication logic
        flash("Login successful!", "success")
        return redirect(url_for("home"))
    return render_template("auth/login.html")

@auth.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        name = request.form.get("name")
        enrollment_id = request.form.get("enrollment_id")
        div = request.form.get("div")
        course = request.form.get("course")
        gender = request.form.get("gender")
        admission_number = request.form.get("admission_number")
        year_of_admission = request.form.get("year_of_admission")
        department = request.form.get("department")
        email = request.form.get("email")
        password = request.form.get("password")

        # Auto-semester calculation
        current_year = datetime.now().year
        years_passed = current_year - int(year_of_admission)
        semester = (years_passed * 2) + 1

        flash(f"Student registered successfully! Assigned Semester: {semester}", "success")
        return redirect(url_for("auth.register_student"))

    return render_template("auth/register.html", current_year=datetime.now().year)

@auth.route("/reset_password", methods=["GET", "POST"])
def reset_password():
    if request.method == "POST":
        # TODO: Add password reset logic
        flash("Password reset email sent!", "info")
        return redirect(url_for("auth.login"))
    return render_template("auth/reset_password.html")

@auth.route("/logout")
def logout():
    # TODO: Add logout logic
    flash("You have been logged out.", "info")
    return redirect(url_for("home"))
