import cx_Oracle



def user_info(id):
    dsn = cx_Oracle.makedsn('localhost', 1521, 'xe')
    conn = cx_Oracle.connect('minipro', 'dbdb', dsn)
    cursor = conn.cursor()

    # 첫 번째 쿼리: ud_dis를 가져오는 쿼리
    sql = """
        select ud_dis
        from userdis
        where ud_id = :id
    """
    cursor.execute(sql, id=id)
    rows = cursor.fetchall()
    ud_dis_list = [item[0] for item in rows]

    disease_list = []
    for name in ud_dis_list:
        # 두 번째 쿼리: dis_middle을 가져오는 쿼리
        sql = """
            select dis_middle 
            from disease
            where dis_id = :name
        """
        cursor.execute(sql, name=name)
        rows = cursor.fetchall()
        if rows:  # 두 번째 쿼리 결과가 존재한다면
            disease_list.append(rows[0][0])  # 첫 번째 결과의 dis_middle 값을 리스트에 추가
    
    
    result_list = []
    for name in disease_list:
        # 세 번째 쿼리: prod_name을 가져오는 쿼리
        sql = """
            select prod_name, prod_eff, prod_min, prod_max, prod_unit, prod_warn
            from prod
            where prod_middle = :name
        """
        cursor.execute(sql, name=name)
        rows = cursor.fetchall()
        if rows:  # 세 번째 쿼리 결과가 존재한다면
            result_list.append({'prod_name': rows[0][0]}) 

    cursor.close()
    conn.close()
    result_list = [dict(t) for t in set(tuple(d.items()) for d in result_list)]
    
    return result_list



def user_info2(id):
    dsn = cx_Oracle.makedsn('localhost', 1521, 'xe')
    conn = cx_Oracle.connect('minipro', 'dbdb', dsn)
    cursor = conn.cursor()

    sql = """
        select md_middle
        from usermiddle
        where md_id = :id
    """
    cursor.execute(sql, id = id)
    rows = cursor.fetchall()
    middle_list = [item[0] for item in rows]
    
    
    result_list = []
    for name in middle_list:
        # 세 번째 쿼리: prod_name을 가져오는 쿼리
        sql = """
            select prod_name
            from prod
            where prod_middle = :name
        """
        cursor.execute(sql, name=name)
        rows = cursor.fetchall()
        if rows:  # 세 번째 쿼리 결과가 존재한다면
            result_list.append({'prod_name': rows[0][0]}) 

    cursor.close()
    conn.close()
    result_list = [dict(t) for t in set(tuple(d.items()) for d in result_list)]
    
    return result_list



def insert_dis(id):
    dsn = cx_Oracle.makedsn('localhost', 1521, 'xe')
    conn = cx_Oracle.connect('minipro', 'dbdb', dsn)
    cursor = conn.cursor()
    sql = """
            select ud_dis
            from userdis
            where ud_id = '{}'
        """.format(id)
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





def insert_middle(id):
    dsn = cx_Oracle.makedsn('localhost', 1521, 'xe')
    conn = cx_Oracle.connect('minipro', 'dbdb', dsn)
    cursor = conn.cursor()
    sql = """
            select md_middle
            from usermiddle
            where md_id = '{}'
        """.format(id)
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




def prod_info(id):
    dsn = cx_Oracle.makedsn('localhost', 1521, 'xe')
    conn = cx_Oracle.connect('minipro', 'dbdb', dsn)
    cursor = conn.cursor()
    sql = """
            select distinct prod_eff , prod_min, prod_max, prod_unit, prod_warn
            from prod
            where prod_name = '{}'
        """.format(id)
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

def prod_info(id):
    dsn = cx_Oracle.makedsn('localhost', 1521, 'xe')
    conn = cx_Oracle.connect('minipro', 'dbdb', dsn)
    cursor = conn.cursor()
    sql = """
            select distinct prod_eff , prod_min, prod_max, prod_unit, prod_warn
            from prod
            where prod_name = :id
        """
    cursor.execute(sql, {"id": id})
    rows = cursor.fetchall()

    cols = [col[0].lower() for col in cursor.description]

    list_dict = [{cols[i]: row[i] for i in range(len(cols))} for row in rows]

    cursor.close()
    conn.close()

    return list_dict


def naver(id):
    dsn = cx_Oracle.makedsn('localhost', 1521, 'xe')
    conn = cx_Oracle.connect('minipro', 'dbdb', dsn)
    cursor = conn.cursor()

    sql = """
        select user_age
        from users
        where user_id = :id
    """
    cursor.execute(sql, {"id": id})
    row = cursor.fetchone()
    user_age = row[0]

    if user_age == '20대':
        sql = """
        select rank, keyword 
        from naver_table
        where age1 = :user_age or age2 = :user_age or age3 = :user_age
        """
    elif user_age == '50대':
        sql = """
        select rank, keyword 
        from naver_table
        where age1 = :user_age or age2 = :user_age
        """
    else:
        sql = """
        select rank, keyword 
        from naver_table
        where age1 = :user_age 
        """

    cursor.execute(sql, {"user_age": user_age})
    rows = cursor.fetchall()

    cols = [col[0].lower() for col in cursor.description]

    list_dict = [{cols[i]: row[i] for i in range(len(cols))} for row in rows]

    cursor.close()
    conn.close()

    return list_dict
