from flask import render_template, redirect, url_for, request, flash
from . import admin

@admin.route("/admin/announcements")
def announcements():
    return render_template("admin/announcements.html")

@admin.route('/admin/base')
def base():
    return render_template("admin/base.html")

@admin.route("/admin/dashboard")
def dashboard():
    return render_template("admin/dashboard.html")

@admin.route("/admin/change_password")
def change_password():
    return render_template("admin/change_password.html")


@admin.route("/admin/ip_management")
def ip_management():
    return render_template("admin/ip_management.html")

@admin.route("/admin/leave_management")
def leave_management():
    return render_template("admin/leave_management.html")

@admin.route("/admin/manage_classes")
def manage_classes():
    return render_template("admin/manage_classes.html")

@admin.route("/admin/manage_courses")
def manage_courses():
    return render_template("admin/manage_courses.html")

@admin.route("/admin/manage_faculty")
def manage_faculty():
    return render_template("admin/manage_faculty.html")

@admin.route("/admin/manage_students")
def manage_students():
    return render_template("admin/manage_students.html")

@admin.route("/admin/manage_subjects")
def manage_subjects():
    return render_template("admin/manage_subject.html")

@admin.route("/admin/manage_timetable")
def manage_timetable():
    return render_template("admin/manage_timetable.html")

@admin.route("/admin/settings")
def settings():
    return render_template("admin/settings.html")
