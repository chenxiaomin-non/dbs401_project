import mysql.connector as conn

def get_connection():
    return conn.connect(
        host="localhost",
        port=3306,
        username="tnn404",
        password="dmPhiTruong",
        database="dbs401_lab7"
    )

