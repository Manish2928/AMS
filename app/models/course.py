class Course:
    def __init__(self, course_id=None, course_name="", course_code="", department_id=None, description="", created_time=None):
        self.course_id = course_id
        self.course_name = course_name
        self.course_code = course_code
        self.department_id = department_id
        self.description = description
        self.created_time = created_time

    def to_tuple(self):
        return (
            self.course_name,
            self.course_code,
            self.department_id,
            self.description
        )


