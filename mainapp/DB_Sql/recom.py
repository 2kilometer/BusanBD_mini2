import cx_Oracle


    
    
def user_info (id):
    dsn = cx_Oracle.makedsn('localhost', 1521, 'xe')
    conn = cx_Oracle.connect('minipro', 'dbdb', dsn)
    cursor = conn.cursor()
    
    sql = """
        select ud_dis 
        from userdis
        where ud_id = '{}'
    """.format(id)
    cursor.execute(sql)
    row = cursor.fetchall()
    
    cursor.close()
    conn.close()