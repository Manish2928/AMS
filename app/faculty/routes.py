from flask import render_template, redirect, url_for, request, flash
from app.utils.decorators import login_required, roles_required
from . import faculty

@faculty.route("/dashboard")
@login_required
@roles_required("faculty")
def dashboard():
    return render_template("faculty/dashboard.html")

@faculty.route('/students')
@login_required
@roles_required("faculty")
def students():
    return render_template("faculty/students.html")

@faculty.route("/report")
@login_required
@roles_required("faculty")
def report():
    return render_template("faculty/report.html")

@faculty.route("/change_password")
@login_required
@roles_required("faculty")
def change_password():
    return render_template("faculty/change_password.html")


@faculty.route("/leave")
@login_required
@roles_required("faculty")
def leave():
    return render_template("faculty/leave.html")

@faculty.route("/profile")
@login_required
@roles_required("faculty")
def profile():
    return render_template("faculty/profile.html")

@faculty.route("/generate_qr")
@login_required
@roles_required("faculty")
def generate_qr():
    return render_template("faculty/generate_qr.html")

@faculty.route("/timetable")
@login_required
@roles_required("faculty")
def timetable():
    return render_template("faculty/timetable.html")

@faculty.route("/generate_qr/qr_generated")
@login_required
@roles_required("faculty")
def qr_generated():
    return render_template("faculty/qr_generated.html")

@faculty.route("/base")
@login_required
@roles_required("faculty")
def base():
    return render_template("faculty/base.html")