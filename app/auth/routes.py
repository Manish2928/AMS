from flask import render_template, request, redirect, url_for, flash, session
from app.auth import auth
from app.auth.forms import LoginForm, AdminRegisterStudentForm, AdminRegisterFacultyForm, ResetPasswordForm, ChangePasswordForm
from app.db_queries import admin_queries
from app.utils.security import hash_password, verify_password
from app.utils.decorators import login_required, roles_required
from app.auth.forms import NewPasswordForm
from app.db_queries import admin_queries
from app.auth.utils import consume_reset_token
import os



# ---------- LOGIN ----------
@auth.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():  # this already checks request.method == POST
        email = form.email.data.strip().lower()
        user = admin_queries.get_user_by_email(email)

        if user and verify_password(form.password.data, user["password_hash"]) and user.get("is_active", 1):
            # reset session & set identity
            session.clear()
            session["user_id"] = user["user_id"]
            session["email"] = user["email"]
            session["role"] = (user.get("role") or user.get("user_type") or "").lower()
            session["user_type"] = (user.get("user_type") or "").lower()

            flash("Welcome!", "success")

            role = session["role"]
            if role == "admin":
                return redirect(url_for("admin.dashboard"))
            elif role == "faculty":
                return redirect(url_for("faculty.dashboard"))
            elif role == "student":
                return redirect(url_for("student.dashboard"))
            flash("Unknown role. Contact admin.", "danger")
            return redirect(url_for("auth.login"))

        flash("Invalid email or password.", "danger")

    return render_template("auth/login.html", form=form)


# ---------- LOGOUT ----------
@auth.route("/logout")
@login_required
def logout():
    session.clear()
    flash("Logged out.", "info")
    return redirect(url_for("auth.login"))

# ---------- ADMIN: REGISTER STUDENT ----------
@auth.route("/admin/register-student", methods=["GET", "POST"])
@roles_required("admin")
def admin_register_student():
    form = AdminRegisterStudentForm()
    if request.method == "POST" and form.validate_on_submit():
        # 1) Create user
        if admin_queries.get_user_by_email(form.email.data):
            flash("Email already registered.", "warning")
            return render_template("auth/register.html", form=form, user_type="student")

        user_id = admin_queries.create_user(
            user_type="student",
            role="student",
            email=form.email.data.strip().lower(),
            password_hash=hash_password(form.password.data)
        )
        # 2) Student profile
        admin_queries.create_student_profile(
            user_id=user_id,
            full_name=form.full_name.data,
            enrollment_id=form.enrollment_id.data,
            course_id=form.course_id.data,
            department_id=form.department_id.data,
            year=form.year.data,
            semester=form.semester.data,
            section=form.section.data or "",
            admission_number=form.admission_number.data or "",
            email=form.email.data.strip().lower()
        )
        flash("Student created.", "success")
        return redirect(url_for("auth.admin_register_student"))

    return render_template("auth/register.html", form=form, user_type="student")

# ---------- ADMIN: REGISTER FACULTY ----------
@auth.route("/admin/register-faculty", methods=["GET", "POST"])
@roles_required("admin")
def admin_register_faculty():
    form = AdminRegisterFacultyForm()
    if request.method == "POST" and form.validate_on_submit():
        if admin_queries.get_user_by_email(form.email.data):
            flash("Email already registered.", "warning")
            return render_template("auth/register.html", form=form, user_type="faculty")

        user_id = admin_queries.create_user(
            user_type="faculty",
            role="faculty",
            email=form.email.data.strip().lower(),
            password_hash=hash_password(form.password.data)
        )
        admin_queries.create_faculty_profile(
            user_id=user_id,
            faculty_name=form.faculty_name.data,
            faculty_id_code=form.faculty_id_code.data,
            department_id=form.department_id.data,
            email=form.email.data.strip().lower()
        )
        flash("Faculty created.", "success")
        return redirect(url_for("auth.admin_register_faculty"))

    return render_template("auth/register.html", form=form, user_type="faculty")

# ---------- ADMIN: RESET PASSWORD (send token) ----------
@auth.route("/reset-password", methods=["GET", "POST"])
# @roles_required("admin")
def admin_reset_password():
    form = ResetPasswordForm()
    publicKey_api = os.getenv("My_publicKey_api")
    service_api = os.getenv("Emailjs_service_api")
    template_api = os.getenv("em_template_api")
    if request.method == "POST" and form.validate_on_submit():
        user = admin_queries.get_user_by_email(form.email.data.strip().lower())
        if not user:
            flash("No user with that email.", "warning")
            return render_template("auth/reset_password.html", form=form)

        from app.auth.utils import generate_reset_token, send_reset_email
        token = generate_reset_token(user["user_id"])
        reset_link = send_reset_email(user["email"], token)

        # Pass reset link + email to template for EmailJS
        return render_template("auth/reset_password.html", form=form, reset_link=reset_link, user_email=user["email"], publicKey_api=publicKey_api, service_api=service_api, template_api=template_api)

    return render_template("auth/reset_password.html", form=form, publicKey_api=publicKey_api, service_api=service_api, template_api=template_api)


# ---------- CONFIRM RESET (dev helper) ----------
@auth.route("/reset-confirm", methods=["GET", "POST"])
def reset_confirm():
    token = request.args.get("token")
    if not token:
        flash("Missing reset token.", "danger")
        return redirect(url_for("auth.admin_reset_password"))

    user = admin_queries.get_user_by_token(token)
    if not user:
        flash("Invalid or expired reset link.", "danger")
        return redirect(url_for("auth.admin_reset_password"))

    form = NewPasswordForm()
    if form.validate_on_submit():
        if consume_reset_token(user["user_id"], form.password.data):
            flash("Password has been reset. You can now log in.", "success")
            return redirect(url_for("auth.login"))
        else:
            flash("This reset link has already been used.", "warning")
            return redirect(url_for("auth.admin_reset_password"))
    print(f"[DEBUG] Looking up token {token}")
    return render_template("auth/reset_confirm.html", form=form, user=user)
    
# ---------- CHANGE PASSWORD (Student/Faculty/Admin) ----------
@auth.route("/change-password", methods=["GET", "POST"])
@login_required
def change_password():
    form = ChangePasswordForm()
    if request.method == "POST" and form.validate_on_submit():
        user = admin_queries.get_user_by_email(session.get("email")) if session.get("email") else None
        # If you didn’t store email in session, fetch by user_id:
        if not user:
            from app.config.db_config import get_db_connection
            conn = get_db_connection()
            cur = conn.cursor(dictionary=True)
            cur.execute("SELECT * FROM USERS WHERE user_id=%s", (session["user_id"],))
            user = cur.fetchone()
            cur.close(); conn.close()

        if not user or not verify_password(form.old_password.data, user["password_hash"]):
            flash("Old password is incorrect.", "danger")
            return render_template("auth/change_password.html", form=form)

        new_hash = hash_password(form.new_password.data)
        admin_queries.update_user_password(user["user_id"], new_hash)
        flash("Password changed.", "success")
        return redirect(url_for("auth.change_password"))

    return render_template("auth/change_password.html", form=form)


