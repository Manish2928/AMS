from flask import render_template
from . import student
from app.utils.decorators import login_required, roles_required

@student.route("/dashboard")
@login_required
@roles_required("student")
def dashboard():
    return render_template("student/dashboard.html")

@student.route('/attendance')
@login_required
@roles_required("student")
def attendance():
    return render_template("student/attendance.html")

@student.route("/change_ip")
@login_required
@roles_required("student")
def change_ip():
    return render_template("student/change_ip.html")

@student.route("/change_password")
@login_required
@roles_required("student")
def change_password():
    return render_template("student/change_password.html")

@student.route("/leave")
@login_required
@roles_required("student")
def leave():
    return render_template("student/leave.html")

@student.route("/profile")
@login_required
@roles_required("student")
def profile():
    return render_template("student/profile.html")

@student.route("/scan_qr")
@login_required
@roles_required("student")
def scan_qr():
    return render_template("student/scan_qr.html")

@student.route("/timetable")
@login_required
@roles_required("student")
def timetable():
    return render_template("student/timetable.html")

@student.route("/base")
def base():
    return render_template("student/base.html")
