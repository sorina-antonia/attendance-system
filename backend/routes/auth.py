from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from db.connection import get_db

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.json
    print("DEBUG RECEIVED DATA:", data)

    name = data.get("username")
    email = data.get("email")
    password = data.get("password")

    if not name or not email or not password:
        return jsonify({"message": "Missing fields"}), 400

    hashed_password = generate_password_hash(password)

    conn = get_db()
    cursor = conn.cursor()

    try:
        cursor.execute("""
            INSERT INTO users (name, email, password_hash)
            VALUES (%s, %s, %s)
        """, (name, email, hashed_password))
        conn.commit()
    except Exception as e:
        return jsonify({"message": "Error: " + str(e)}), 500
    finally:
        cursor.close()
        conn.close()

@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    print("DEBUG LOGIN DATA:", data)

    email = data.get("email")
    password = data.get("password")

    if not email or not password:
        return jsonify({"message": "Missing fields"}), 400

    conn = get_db()
    cursor = conn.cursor()

    try:
        cursor.execute("SELECT id, name, email, password_hash, role FROM users WHERE email = %s", (email,))
        user = cursor.fetchone()

        if not user:
            return jsonify({"message": "User not found"}), 404

        # ✔ THIS MUST BE HERE, properly aligned
        user_id, name, email, password_hash, role = user

        if not check_password_hash(password_hash, password):
            return jsonify({"message": "Incorrect password"}), 401

        return jsonify({
            "message": "Login successful",
            "user": {
                "id": user_id,
                "name": name,
                "email": email,
                "role": role
            }
        }), 200

    except Exception as e:
        return jsonify({"message": "Error: " + str(e)}), 500

    finally:
        cursor.close()
        conn.close()


    return jsonify({"message": "User registered successfully"}), 201
    return jsonify({"message": "User registered successfully"})
