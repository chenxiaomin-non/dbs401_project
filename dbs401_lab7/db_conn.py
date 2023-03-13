import mysql.connector as conn

def get_connection():
    return conn.connect(
        host="localhost",
        port=3306,
        username="root",
        password="root",
        database="mydb"
    )

