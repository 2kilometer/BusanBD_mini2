import cx_Oracle

### test 함수 만들기
def testData() :
    return "홍길동"

### DB 조회
"""
-- 조회컬럼 : 회원이름, 주문일자(0000-00-00 형태), 상품명
                    :  조건, 상품명에 "컴퓨터"가 포함된 경우
                    :  정렬은 회원이름을 기준으로 오름차순
"""
def mem_List():
    dsn = cx_Oracle.makedsn('localhost', 1521, 'xe')
    conn = cx_Oracle.connect('busan', 'dbdb', dsn)
    cursor = conn.cursor()
    
    sql = """
            Select mem_name, 
                    to_char(to_date(substr(cart_no, 1, 8)), 'yyyy-mm-dd') as cart_date,
                    prod_name
            From member, cart, prod
            Where mem_id = cart_member
            And prod_id = cart_prod
            And prod_name like '%컴퓨터%'
            Order By mem_name ASC
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