from flask import render_template
from app.utils.decorators import login_required, roles_required
from . import admin

@admin.route("/announcements")
@login_required
@roles_required("admin")
def announcements():
    return render_template("admin/announcements.html")

@admin.route('/base')
@login_required
@roles_required("admin")
def base():
    return render_template("admin/base.html")

@admin.route("/dashboard")
@login_required
@roles_required("admin")
def dashboard():
    return render_template("admin/dashboard.html")

@admin.route("/change_password")
@login_required
@roles_required("admin")
def change_password():
    return render_template("admin/change_password.html")

@admin.route("/ip_management")
@login_required
@roles_required("admin")
def ip_management():
    return render_template("admin/ip_management.html")

@admin.route("/leave_management")
@login_required
@roles_required("admin")
def leave_management():
    return render_template("admin/leave_management.html")

@admin.route("/manage_classes")
@login_required
@roles_required("admin")
def manage_classes():
    return render_template("admin/manage_classes.html")

@admin.route("/manage_courses")
@login_required
@roles_required("admin")
def manage_courses():
    return render_template("admin/manage_courses.html")

@admin.route("/manage_faculty")
@login_required
@roles_required("admin")
def manage_faculty():
    return render_template("admin/manage_faculty.html")

@admin.route("/manage_students")
@login_required
@roles_required("admin")
def manage_students():
    return render_template("admin/manage_students.html")

@admin.route("/manage_subjects")
@login_required
@roles_required("admin")
def manage_subjects():
    return render_template("admin/manage_subject.html")

@admin.route("/manage_timetable")
@login_required
@roles_required("admin")
def manage_timetable():
    return render_template("admin/manage_timetable.html")

@admin.route("/settings")
@login_required
@roles_required("admin")
def settings():
    return render_template("admin/settings.html")
