from flask import Blueprint, jsonify
from db.connection import get_db

students_bp = Blueprint('students', __name__)

@students_bp.route("/students", methods=["GET"])
def get_students():
    print("DB connected, running SELECT...")
    
    conn = get_db()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()

    cursor.close()
    conn.close()

    return jsonify(students)
