import streamlit as st
import sqlite3
import pandas as pd
import os

# SQLite DB 파일 경로
DB_PATH = "classicmodels.sqlite"  # 파일이 있는 경로에 맞게 수정하세요

# 쿼리 실행 함수
def fetch_data(query):
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
        columns = [col[0] for col in cursor.description]
        return pd.DataFrame(rows, columns=columns)
    except Exception as e:
        st.error(f"❌ 쿼리 오류: {e}")
        return pd.DataFrame()
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'conn' in locals():
            conn.close()

# Streamlit UI
st.title("📦 ClassicModels Dashboard (SQLite)")

# SQL 입력창
user_query = st.text_area("📝 SQL 쿼리를 입력하세요:", "SELECT * FROM customers LIMIT 10;")

# 실행 버튼
if st.button("실행"):
    st.write("💡 실행된 쿼리:")
    st.code(user_query, language='sql')

    result_df = fetch_data(user_query)
    if not result_df.empty:
        st.success(f"✅ {len(result_df)}개 행 조회됨")
        st.dataframe(result_df)
    else:
        st.warning("⚠️ 결과가 없거나 쿼리에 오류가 있습니다.")
