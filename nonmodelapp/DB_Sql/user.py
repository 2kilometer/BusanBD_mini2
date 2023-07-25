from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd
import cx_Oracle

def getLoginChk(user_id, user_pw) :
    dsn = cx_Oracle.makedsn('localhost', 1521, 'xe')
    conn = cx_Oracle.connect ('minipro', 'dbdb', dsn)
    cursor = conn.cursor ()
    
    sql = """
        SELECT *
        FROM USERS
        WHERE USER_ID = '{}'
            AND USER_PW = '{}'
    """.format(user_id, user_pw)
    
    cursor.execute (sql)
    row = cursor.fetchone()

    if row == None :
        cursor.close()
        conn.close()
        return {"result" : "None"}
    
    colnames = cursor.description
    
    cols = []
    for col in colnames :
        cols.append(col[0].lower())
    
    dict_row = {}
    for i in range (len(cols)) :
        dict_row[cols[i]] = row[i]
    
    cursor.close()
    conn.close()
    
    return dict_row