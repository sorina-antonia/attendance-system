from flask import Blueprint, jsonify, request
from db.connection import get_db
from datetime import datetime

attendance_bp = Blueprint('attendance', __name__)


# ADMIN
@attendance_bp.route("/attendance", methods=["GET"])
def get_attendance():
    conn = get_db()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("""
        SELECT a.id, a.date, a.time, a.status,
               s.name AS student_name,
               c.name AS class_name
        FROM attendance a
        JOIN students s ON a.student_id = s.id
        JOIN classes c ON a.class_id = c.id
    """)

    records = cursor.fetchall()

    cursor.close()
    conn.close()

    return jsonify(records), 200


# STUDENT: Mark themselves present
@attendance_bp.route("/attendance/mark", methods=["POST"])
def mark_attendance():
    data = request.get_json()
    user = data.get("user")

    if not user:
        return jsonify({"message": "Missing user"}), 400

    if user["role"] != "student":
        return jsonify({"message": "Forbidden"}), 403

    student_id = user["id"]
    class_id = user["class_id"]

    now = datetime.now()
    date = now.date()
    time = now.time()

    conn = get_db()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO attendance (student_id, class_id, date, time, status)
        VALUES (%s, %s, %s, %s, 'Present')
    """, (student_id, class_id, date, time))

    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({"message": "Attendance marked"}), 200


# STUDENT
@attendance_bp.route("/attendance/student", methods=["POST"])
def get_student_attendance():
    data = request.get_json()
    user = data.get("user")

    if not user:
        return jsonify({"message": "Missing user"}), 400

    if user["role"] != "student":
        return jsonify({"message": "Forbidden"}), 403

    student_id = user["id"]

    conn = get_db()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("""
        SELECT date, time, status
        FROM attendance
        WHERE student_id = %s
        ORDER BY date DESC, time DESC
    """, (student_id,))

    rows = cursor.fetchall()

    cursor.close()
    conn.close()

    return jsonify(rows), 200


# TEACHER
@attendance_bp.route("/attendance/class", methods=["POST"])
def get_teacher_class_attendance():
    data = request.get_json()
    user = data.get("user")

    if not user:
        return jsonify({"message": "Missing user"}), 400

    if user["role"] != "teacher":
        return jsonify({"message": "Forbidden"}), 403

    class_id = user["class_id"]

    conn = get_db()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("""
        SELECT a.id, s.name AS student_name, a.date, a.time, a.status
        FROM attendance a
        JOIN students s ON a.student_id = s.id
        WHERE a.class_id = %s
    """, (class_id,))

    rows = cursor.fetchall()

    cursor.close()
    conn.close()

    return jsonify(rows), 200


# TEACHER
@attendance_bp.route("/attendance/update", methods=["POST"])
def update_attendance():
    data = request.get_json()
    user = data.get("user")

    if not user:
        return jsonify({"message": "Missing user"}), 400

    if user["role"] != "teacher":
        return jsonify({"message": "Forbidden"}), 403

    attendance_id = data.get("attendance_id")
    status = data.get("status")

    conn = get_db()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE attendance SET status = %s WHERE id = %s
    """, (status, attendance_id))

    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({"message": "Attendance updated"}), 200
