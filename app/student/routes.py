from flask import render_template, redirect, url_for, request, flash
from . import student

@student.route("/student/dashboard")
def dashboard():
    return render_template("student/dashboard.html")

@student.route('/student/attendance')
def attendance():
    return render_template("student/attendance.html")

@student.route("/student/change_ip")
def change_ip():
    return render_template("student/change_ip.html")

@student.route("/student/change_password")
def change_password():
    return render_template("student/change_password.html")


@student.route("/student/leave")
def leave():
    return render_template("student/leave.html")

@student.route("/student/profile")
def profile():
    return render_template("student/profile.html")

@student.route("/student/scan_qr")
def scan_qr():
    return render_template("student/scan_qr.html")

@student.route("/student/timetable")
def timetable():
    return render_template("student/timetable.html")

@student.route("/base")
def base():
    return render_template("student/base.html")