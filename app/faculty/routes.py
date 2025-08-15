from flask import render_template, redirect, url_for, request, flash
from . import faculty

@faculty.route("/faculty/dashboard")
def dashboard():
    return render_template("faculty/dashboard.html")

@faculty.route('/faculty/students')
def students():
    return render_template("faculty/students.html")

@faculty.route("/faculty/report")
def report():
    return render_template("faculty/report.html")

@faculty.route("/faculty/change_password")
def change_password():
    return render_template("faculty/change_password.html")


@faculty.route("/faculty/leave")
def leave():
    return render_template("faculty/leave.html")

@faculty.route("/faculty/profile")
def profile():
    return render_template("faculty/profile.html")

@faculty.route("/faculty/generate_qr")
def generate_qr():
    return render_template("faculty/generate_qr.html")

@faculty.route("/faculty/timetable")
def timetable():
    return render_template("faculty/timetable.html")

@faculty.route("/faculty/generate_qr/qr_generated")
def qr_generated():
    return render_template("faculty/qr_generated.html")

@faculty.route("/base")
def base():
    return render_template("faculty/base.html")