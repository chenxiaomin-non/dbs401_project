import db_conn

def get_student(id: str) -> list:
    db = db_conn.get_connection()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM students WHERE sid like '" + id + "';")

    # stupid code here: we only need one row
    # so the correct statement should be:
    # result = cursor.fetchone()
    result = cursor.fetchall()

    json_result = []
    for row in result:
        json_result.append({
            "sid": row[1],
            "name": row[2],
            "gpa": row[3],
            "course": row[4],
            "semester": row[5]
        })
    db.close()
    return json_result

def create_table_if_not_exists():
    db = db_conn.get_connection()
    cursor = db.cursor()

    # check if table students exists
    cursor.execute('''show tables like 'students';''')
    result = cursor.fetchall()
    if len(result) > 0:
        return


    cursor.execute('''
        CREATE TABLE IF NOT EXISTS students (
            id int AUTO_INCREMENT PRIMARY KEY,
            sid varchar(10) not null, 
            name VARCHAR(255) not null, 
            gpa float not null,
            course varchar(10) not null,
            semester varchar(10) not null
        );''')
    
    db.commit()

    # insert some dummy data
    cursor.execute('''
        INSERT INTO students VALUES (1, 'CE150740', 'Pham Chi Hai', 9.3, 'MLN111', 'SP23');
        INSERT INTO students VALUES (2, 'CE150740', 'Pham Chi Hai', 9.3, 'IAW401', 'FA22');
        INSERT INTO students VALUES (3, 'CE150505', 'Tran Trieu Tan', 9.1, 'HOD401', 'FA22');
        INSERT INTO students VALUES (4, 'CE150505', 'Tran Trieu Tan', 8.1, 'IAP401', 'FA22');
        INSERT INTO students VALUES (5, 'CE150505', 'Nguyen Hoang My', 8.5, 'IAP401', 'FA22');
        INSERT INTO students VALUES (6, 'CE150505', 'Nguyen Hoang My', 8.1, 'MLN111', 'SP23');
        ''')
    db.commit()
    db.close()
