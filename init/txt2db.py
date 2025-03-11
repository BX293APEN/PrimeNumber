from MySQLite import MySQLite
import os
if __name__ == "__main__":
    initData = f"{os.path.dirname(__file__)}/prime_number.list"
    dbPath = "prime_number.db"
    with MySQLite(dbPath) as database:
        database.send_sql(
            f"""
                CREATE TABLE 素数(
                    ID      INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                    value   INTEGER UNIQUE NOT NULL
                )
            """
        )
        try:
            with open(initData, "r", encoding="shift_jis") as data:
                d = data.read()
            
            for l in d.split("\n"):
                try:
                    database.send_sql(
                        f"""INSERT INTO 素数 (value) VALUES({int(l)})"""
                    )
                except Exception as e:
                    print(f"""ERROR : {l}""")
        except:
            print("初期ファイルがありません")
        finally:
            print("終了")
            with MySQLite(dbPath) as database:
                for rd in database.send_sql("SELECT * FROM 素数"):
                    print(rd)
