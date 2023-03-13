import db_conn

def get_student(id: str) -> list:
    db = db_conn.get_connection()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM students WHERE id = " + id)

    # stupid code here: we only need one row
    # so the correct statement should be:
    # result = cursor.fetchone()
    result = cursor.fetchall()
    return result