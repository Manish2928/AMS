from app.config.db_config import get_db_connection

def get_student_by_user_id(user_id: int):
    conn = get_db_connection()
    if not conn: return None
    try:
        cur = conn.cursor(dictionary=True)
        cur.execute("SELECT * FROM STUDENTS WHERE user_id=%s", (user_id,))
        return cur.fetchone()
    finally:
        cur.close(); conn.close()
