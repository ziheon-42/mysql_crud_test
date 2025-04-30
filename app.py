import streamlit as st
import sqlite3
import pandas as pd

# SQLite3 데이터베이스 연결
conn = sqlite3.connect('classicmodels.db')
c = conn.cursor()

# Streamlit 제목 설정
st.title('Classic Models Dashboard')

# 데이터베이스에서 데이터 가져오기
c.execute("SELECT * FROM customers")
data = c.fetchall()

# 데이터를 pandas DataFrame으로 변환
columns = [description[0] for description in c.description]  # 컬럼 이름 가져오기
df = pd.DataFrame(data, columns=columns)

# 데이터 표시
st.write("Customers Data", df)

# 연결 종료
conn.close()