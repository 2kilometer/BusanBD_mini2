import cx_Oracle

def cart_List():
    dsn = cx_Oracle.makedsn('localhost', 1521, 'xe')
    conn = cx_Oracle.connect('busan', 'dbdb', dsn)
    cursor = conn.cursor()
    
    sql = """
            Select cart_no, cart_member, cart_prod, cart_qty
            From cart
            Order By cart_no Desc
    """    
    cursor.execute(sql)
    rows = cursor.fetchall()
    
    ### 컬럼 데이터 추출하기
    colnames = cursor.description
    
    # 1. 컬럼을 리스트로 변경하기
    # 순수 for문으로만..
    cols = []
    for col in colnames:
        cols.append(col[0].lower())

    
    ### 컬럼을 key로, rows의 각행의 값을 value로 해서
    # - 리스트의 딕셔너리 형태(행/열 데이터)만들기
    list_dict = []
    for row in rows :
        temp_dict = {}
        
        for i in range(len(cols)) :
            temp_dict[cols[i]] = row[i]
        
        list_dict.append(temp_dict)
        
    cursor.close()
    conn.close()
    
    return list_dict