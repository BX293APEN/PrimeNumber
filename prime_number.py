import subprocess, time
from MySQLite import MySQLite



if __name__ == "__main__":
    target = 2 ** 256
    with MySQLite("prime_number.db") as database:
        pData = database.send_sql(
            f"""
                SELECT value FROM 素数 ORDER BY value ASC;
            """
        )

    n = int(pData[-1][0])

    try:
        while n < target:
            subprocess.run("cls", shell=True)
            flag = 0
            print(f"{len(str(n))}桁")
            for p in pData:
                if p[0] ** 2 > n:
                    break
                elif (n % p[0]) == 0:
                    flag = 1
                    break
                
            if flag == 0:
                try:
                    with MySQLite("prime_number.db") as database:
                        database.send_sql(
                            f"""INSERT INTO 素数 (value) VALUES({int(n)})"""
                        )
                except Exception as e:
                    print(e)
            n += 2
            time.sleep(0.01)
            
    except Exception as e:
        input(e)