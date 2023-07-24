import cx_Oracle


### DB 조회
def sign_up(email, pass_word, age, gender, stress):
    dsn = cx_Oracle.makedsn('localhost', 1521, 'xe')
    conn = cx_Oracle.connect('minipro', 'dbdb', dsn)
    cursor = conn.cursor()
    
    sql = """
        INSERT INTO users(user_id, user_pw, user_age, user_gender, user_stress) VALUES('{}','{}','{}','{}','{}')
    """.format(email, pass_word, age, gender, stress)
    cursor.execute(sql)
    
    conn.commit()  # 변경 내용을 데이터베이스에 커밋

    
    cursor.close()
    conn.close()
    
    
def user_disin (ud_id, ud_dis, ud_middle):
    dsn = cx_Oracle.makedsn('localhost', 1521, 'xe')
    conn = cx_Oracle.connect('minipro', 'dbdb', dsn)
    cursor = conn.cursor()
    
    sql = """
        INSERT INTO users(user_id, user_pw, user_age, user_gender, user_stress) VALUES('{}','{}','{}')
    """.format()
    cursor.execute(ud_id, ud_dis, ud_middle)
    
    conn.commit()  # 변경 내용을 데이터베이스에 커밋

    
    cursor.close()
    conn.close()
