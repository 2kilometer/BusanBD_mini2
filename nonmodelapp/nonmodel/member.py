import cx_Oracle

### 회원 로그인 처리에 사용..
def getLoginChk(mem_id, mem_pass):
    dsn = cx_Oracle.makedsn('localhost', 1521, 'xe')
    conn = cx_Oracle.connect('busan', 'dbdb', dsn)
    cursor = conn.cursor()
    
    sql = """
            Select mem_id, mem_pass, mem_name
            From member
            Where mem_id = '{}'
            And mem_pass = '{}'
        """.format(mem_id, mem_pass)   
         
    cursor.execute(sql)
    
    ### ('a001', '1357', '김은대')
    row = cursor.fetchone()
    
    ### 조회결과가 없으면,,, 아래 처리 안하고 return 시키기
    # - 회원정보가 없는 회원으로 판단하기
    if row == None :
        cursor.close()
        conn.close()
        return {"result" : "None"}
    
    ### 컬럼 데이터 추출하기
    colnames = cursor.description
    
    # 1. 컬럼을 리스트로 변경하기
    # 순수 for문으로만..
    cols = []
    for col in colnames:
        cols.append(col[0].lower())

    
    ### 딕셔너리 형태로 변환하기
    # {'mem_id':'a001', 'mem_pass':'1357', 'mem_name':'김은대'}
    dict_row = {}          
    for i in range(len(cols)) :
        dict_row[cols[i]] = row[i]
        
    cursor.close()
    conn.close()
    
    return dict_row