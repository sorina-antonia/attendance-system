from flask import Blueprint, jsonify
from db.connection import get_db

courses_bp = Blueprint('courses', __name__)

@courses_bp.route("/courses", methods=["GET"])
def get_courses():
    print("DB connected, running SELECT for courses...")

    conn = get_db()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM courses")
    courses = cursor.fetchall()

    cursor.close()
    conn.close()

    return jsonify(courses)
