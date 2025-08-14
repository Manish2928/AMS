from flask import Blueprint, jsonify
from app.config.db_config import get_db_connection

test_db = Blueprint("test_db", __name__)

@test_db.route("/test-db")
def test_database():
    conn = get_db_connection()
    if not conn:
        return jsonify({"status": "error", "message": "Database connection failed"}), 500

    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT DATABASE() as db_name;")
    result = cursor.fetchone()

    cursor.close()
    conn.close()

    return jsonify({"status": "success", "database": result['db_name']})
