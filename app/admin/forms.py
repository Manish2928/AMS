from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length


class CreateCourseForm(FlaskForm):
    course_name = StringField("Course Name", validators=[DataRequired(), Length(max=255)])
    course_code = StringField("Course Code", validators=[DataRequired(), Length(max=50)])
    department_id = IntegerField("Department ID", validators=[DataRequired()])
    description = TextAreaField("Description", validators=[Length(max=1000)])
    submit = SubmitField("Create Course")


