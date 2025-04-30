# 📦 ClassicModels Dashboard (SQLite)
🖼️ **Streamlit**을 사용하여 **SQLite** 데이터베이스에서 데이터를 쿼리하고 시각화하는 대시보드
![Image](https://github.com/user-attachments/assets/1071752a-601f-4dba-8da0-36aa3568255c)

## 🛠️ 필수 라이브러리
- `streamlit`
- `sqlite3`
- `pandas`


## 🔧 설치 방법
- 로컬 환경에서 프로젝트를 실행하려면 먼저 아래 shlell을 실행하여 가상환경 접속
```bash
./setup-virtualenv.sh
```
- 필요 라이브러리 설치
```bash
pip install -r requirements.txt
```


## 🖼️ 대시보드 실행(코드로 접속)
- 라이브러리 설치가 완료되면 아래 코드를 입력하여 대시보드 실행 가능
- 대시보드가 실행되면 **http://localhost:8501** 으로 접속됨
```bash
streamlit run streamlit_sqlite_app.py
```


## 🌐 대시보드 실행(링크로 접속)
[대시보드 확인하기](https://lgu6sql-dfeqfqnwtwmqmwa2xktbnb.streamlit.app/)


## 🖼️ 데이터 분석 시각화 샘플
- [customers_by_country.png]![Image](https://github.com/user-attachments/assets/f0fc8815-4625-40f6-b650-f6e9a1eb71d0)

- [order_amounts_distribution]![Image](https://github.com/user-attachments/assets/b9a38d40-c214-4310-8515-4d71366a1ec0)

- [orders_by_month]![Image](https://github.com/user-attachments/assets/6260129f-f338-4d33-be78-22d51d0c7d1f)

- [product_prices]![Image](https://github.com/user-attachments/assets/e432e3d7-789a-4181-aa31-05cd968c98e5)