import cx_Oracle


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
    
    
def ud_dis (ud_id, ud_dis):
    dsn = cx_Oracle.makedsn('localhost', 1521, 'xe')
    conn = cx_Oracle.connect('minipro', 'dbdb', dsn)
    cursor = conn.cursor()
    
    sql = """
        INSERT INTO userdis(ud_id, ud_dis) 
        VALUES('{}' ,'{}')
    """.format(ud_id, ud_dis)
    cursor.execute(sql)
    
    conn.commit()  # 변경 내용을 데이터베이스에 커밋

    
    cursor.close()
    conn.close()
    
    
def middle (id, middle):
    dsn = cx_Oracle.makedsn('localhost', 1521, 'xe')
    conn = cx_Oracle.connect('minipro', 'dbdb', dsn)
    cursor = conn.cursor()
    
    sql = """
        INSERT INTO usermiddle(md_id, md_middle) 
        VALUES('{}','{}')
    """.format(id, middle)
    cursor.execute(sql)
    
    conn.commit()  # 변경 내용을 데이터베이스에 커밋

    
    cursor.close()
    conn.close()