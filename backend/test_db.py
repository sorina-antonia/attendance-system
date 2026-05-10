from db.connection import get_connection

conn = get_connection()

if conn:
    print("Connected successfully!")
else:
    print("Connection failed.")
