import pandas as pd
from sqlalchemy import create_engine


# 엑셀 파일을 데이터프레임으로 읽기
df = pd.read_excel('/prod에 들어갈 내용.xlsx')

# 데이터프레임을 SQL 테이블로 삽입
df.to_sql('prod', con=engine, if_exists='append', index=False)
