import sqlite3, os, copy

class MySQLite():
    def __init__(self, db = f"{os.path.dirname(__file__)}/sqlite3.db"):
        # データベースとの接続
        self.databaseHost = sqlite3.connect(database = db)
    
    def __enter__(self):
        # カーソルを作る
        self.database = self.databaseHost.cursor()
        return self
    
    def send_sql(self, sql): # SQL文送信
        self.database.execute(sql)
        self.db_commit()
        return self.database.fetchall() # タプル形式で全て取得
    
    def db_commit(self):
        self.databaseHost.commit()

    def __exit__(self, *args):
        self.db_commit()
        self.database.close()
        self.databaseHost.close()

class Data:
    sql = ""

if __name__ == "__main__":
    with MySQLite("prime_number.db") as database:
        while True:
            sql = input("sqlite3 > ")
            while True:
                Data.sql += f"{sql} "
                if sql.count(";") > 0 or sql == "":
                    sql = copy.deepcopy(Data.sql)
                    Data.sql = ""
                    break
                sql = input("    - > ")
                
            if sql.count("quit") > 0:
                break
            try:
                for rd in database.send_sql(sql):
                    print(rd)
                    
            except Exception as e:
                print(e)

    
    input("Bye")