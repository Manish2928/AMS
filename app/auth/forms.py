from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField, IntegerField
from wtforms.validators import DataRequired, Email, Length, Optional

class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email(), Length(max=100)])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=6, max=128)])
    submit = SubmitField("Login")

class AdminRegisterStudentForm(FlaskForm):
    full_name = StringField("Name", validators=[DataRequired(), Length(max=150)])
    enrollment_id = StringField("Enrollment ID", validators=[DataRequired(), Length(max=50)])
    course_id = IntegerField("Course ID", validators=[DataRequired()])
    department_id = IntegerField("Department ID", validators=[DataRequired()])
    year = IntegerField("Year", validators=[DataRequired()])
    semester = IntegerField("Semester", validators=[DataRequired()])
    section = StringField("Div", validators=[Optional(), Length(max=10)])
    admission_number = StringField("Admission number", validators=[Optional(), Length(max=50)])
    email = StringField("Email", validators=[DataRequired(), Email(), Length(max=100)])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=6, max=128)])
    submit = SubmitField("Create")

class AdminRegisterFacultyForm(FlaskForm):
    faculty_name = StringField("Name", validators=[DataRequired(), Length(max=150)])
    faculty_id_code = StringField("Faculty Code", validators=[DataRequired(), Length(max=50)])
    department_id = IntegerField("Department ID", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email(), Length(max=100)])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=6, max=128)])
    submit = SubmitField("Create")

class ResetPasswordForm(FlaskForm):
    email = StringField("User Email", validators=[DataRequired(), Email()])
    submit = SubmitField("Send Reset Link")

class ChangePasswordForm(FlaskForm):
    old_password = PasswordField("Old Password", validators=[DataRequired()])
    new_password = PasswordField("New Password", validators=[DataRequired(), Length(min=6)])
    submit = SubmitField("Change Password")

class NewPasswordForm(FlaskForm):
    password = PasswordField("New Password", validators=[DataRequired(), Length(min=6, max=128)])
    submit = SubmitField("Set New Password")
