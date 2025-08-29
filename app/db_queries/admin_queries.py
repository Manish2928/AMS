from app.config.db_config import get_db_connection

# -------- USERS ----------
def get_user_by_email(email: str):
    conn = get_db_connection()
    if not conn: return None
    try:
        cur = conn.cursor(dictionary=True)
        cur.execute("SELECT * FROM USERS WHERE email=%s", (email,))
        return cur.fetchone()
    finally:
        cur.close(); conn.close()

def create_user(user_type: str, role: str, email: str, password_hash: str):
    conn = get_db_connection()
    if not conn: return None
    try:
        cur = conn.cursor()
        cur.execute("""
            INSERT INTO USERS (user_type, role, email, password_hash, is_active)
            VALUES (%s, %s, %s, %s, 1)
        """, (user_type, role, email, password_hash))
        conn.commit()
        return cur.lastrowid
    finally:
        cur.close(); conn.close()

def set_password_reset_token(user_id: int, token: str, expiry_dt):
    conn = get_db_connection()
    if not conn: return False
    try:
        cur = conn.cursor()
        cur.execute("""
            UPDATE USERS SET password_reset_token=%s, token_expiry=%s WHERE user_id=%s
        """, (token, expiry_dt, user_id))
        conn.commit()
        return cur.rowcount > 0
    finally:
        cur.close(); conn.close()

def clear_reset_token(user_id: int):
    conn = get_db_connection()
    if not conn: return False
    try:
        cur = conn.cursor()
        cur.execute("""
            UPDATE USERS SET password_reset_token=NULL, token_expiry=NULL WHERE user_id=%s
        """, (user_id,))
        conn.commit()
        return True
    finally:
        cur.close(); conn.close()

def update_user_password(user_id: int, new_hash: str):
    conn = get_db_connection()
    if not conn: return False
    try:
        cur = conn.cursor()
        cur.execute("UPDATE USERS SET password_hash=%s WHERE user_id=%s", (new_hash, user_id))
        conn.commit()
        return cur.rowcount > 0
    finally:
        cur.close(); conn.close()

# -------- STUDENTS ----------
from app.config.db_config import get_db_connection

# -------- USERS ----------
def get_user_by_email(email: str):
    conn = get_db_connection()
    if not conn: return None
    try:
        cur = conn.cursor(dictionary=True)
        cur.execute("SELECT * FROM USERS WHERE email=%s", (email,))
        return cur.fetchone()
    finally:
        cur.close(); conn.close()

def create_user(user_type: str, role: str, email: str, password_hash: str):
    conn = get_db_connection()
    if not conn: return None
    try:
        cur = conn.cursor()
        cur.execute("""
            INSERT INTO USERS (user_type, role, email, password_hash, is_active)
            VALUES (%s, %s, %s, %s, 1)
        """, (user_type, role, email, password_hash))
        conn.commit()
        return cur.lastrowid
    finally:
        cur.close(); conn.close()

def set_password_reset_token(user_id: int, token: str, expiry):
    conn = get_db_connection()
    if not conn:
        return
    try:
        cur = conn.cursor()
        cur.execute("""
            UPDATE USERS
            SET password_reset_token = %s,
                token_expiry = %s
            WHERE user_id = %s
        """, (token, expiry, user_id))
        conn.commit()   # <-- MUST commit
    finally:
        cur.close(); conn.close()


def get_user_by_token(token: str):
    conn = get_db_connection()
    if not conn:
        return None
    try:
        cur = conn.cursor(dictionary=True)
        cur.execute("""
            SELECT * FROM USERS
            WHERE password_reset_token = %s
              AND token_expiry > UTC_TIMESTAMP()
        """, (token,))
        return cur.fetchone()
    finally:
        cur.close(); conn.close()



def clear_reset_token(user_id: int):
    conn = get_db_connection()
    if not conn: return False
    try:
        cur = conn.cursor()
        cur.execute("""
            UPDATE USERS SET password_reset_token=NULL, token_expiry=NULL WHERE user_id=%s
        """, (user_id,))
        conn.commit()
        return True
    finally:
        cur.close(); conn.close()

def update_user_password(user_id: int, new_hash: str):
    conn = get_db_connection()
    if not conn: return False
    try:
        cur = conn.cursor()
        cur.execute("UPDATE USERS SET password_hash=%s WHERE user_id=%s", (new_hash, user_id))
        conn.commit()
        return cur.rowcount > 0
    finally:
        cur.close(); conn.close()

# -------- STUDENTS ----------
def create_student_profile(user_id: int, full_name: str, enrollment_id: str,
                           course_id: int, department_id: int, year: int,
                           semester: int, section: str, admission_number: str, email: str):
    conn = get_db_connection()
    if not conn: return None
    try:
        cur = conn.cursor()
        cur.execute("""
            INSERT INTO STUDENTS 
                (user_id, full_name, enrollment_id, course_id, department_id, year, semester, section, admission_number, email)
            VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
        """, (user_id, full_name, enrollment_id, course_id, department_id, year, semester, section, admission_number, email))
        conn.commit()
        return cur.lastrowid
    finally:
        cur.close(); conn.close()

# -------- FACULTY ----------
def create_faculty_profile(user_id: int, faculty_name: str, faculty_id_code: str,
                           department_id: int, email: str):
    conn = get_db_connection()
    if not conn: return None
    try:
        cur = conn.cursor()
        cur.execute("""
            INSERT INTO FACULTY (user_id, faculty_name, faculty_id_code, department_id, email)
            VALUES (%s,%s,%s,%s,%s)
        """, (user_id, faculty_name, faculty_id_code, department_id, email))
        conn.commit()
        return cur.lastrowid
    finally:
        cur.close(); conn.close()


# -------- FACULTY ----------
def create_faculty_profile(user_id: int, faculty_name: str, faculty_id_code: str,
                           department_id: int, email: str):
    conn = get_db_connection()
    if not conn: return None
    try:
        cur = conn.cursor()
        cur.execute("""
            INSERT INTO FACULTY (user_id, faculty_name, faculty_id_code, department_id, email)
            VALUES (%s,%s,%s,%s,%s)
        """, (user_id, faculty_name, faculty_id_code, department_id, email))
        conn.commit()
        return cur.lastrowid
    finally:
        cur.close(); conn.close()


# -------- COURSES ----------
def create_course(course_name: str, course_code: str, department_id: int, description: str | None = None):
    conn = get_db_connection()
    if not conn:
        return None
    
    try:
        cur = conn.cursor(dictionary=True)

         # Optional: Check duplicate manually before insert
        cur.execute("SELECT course_id FROM COURSES WHERE course_code = %s AND department_id = %s", 
                    (course_code, department_id))
        existing = cur.fetchone()
        if existing:
            return(f"Course with code '{course_code}' already exists in this department.", "warning")
            
        
        # ✅ Check if department exists
        cur.execute("SELECT 1 FROM departments WHERE department_id = %s", (department_id,))
        if cur.fetchone() is None:
            return {"error": f"Department ID {department_id} does not exist. Please enter a valid department."}

        # ✅ Insert course only if department is valid
        cur.execute(
            """
            INSERT INTO courses (course_name, course_code, department_id, description)
            VALUES (%s, %s, %s, %s)
            """,
            (course_name, course_code, department_id, description)
        )
        conn.commit()
        return {"course_id": cur.lastrowid}

    finally:
        cur.close()
        conn.close()

