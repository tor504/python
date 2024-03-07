import sqlite3

def read_from_db_file(database_file):
    try:
        # 데이터베이스 연결
        conn = sqlite3.connect(database_file)
        cursor = conn.cursor()

        # 데이터베이스에서 가상화폐 정보 읽어오기
        cursor.execute("SELECT * FROM crypto_prices")
        rows = cursor.fetchall()

        # 데이터 출력
        print("가상화폐 정보:")
        for row in rows:
            print(row)

        # 연결 닫기
        conn.close()
    except sqlite3.Error as e:
        print("SQLite 오류:", e)

if __name__ == "__main__":
    database_file = "crypto_prices.db"  # 데이터베이스 파일 경로
    read_from_db_file(database_file)