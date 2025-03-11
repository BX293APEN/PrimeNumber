import subprocess, time
from MySQLite import MySQLite
from multiprocessing import Process, Value

def disp(endFlag):
    dbFile = "prime_number.db"
    while endFlag.value == 0:
        with MySQLite(dbFile) as database:
            pData = database.send_sql(
                f"""
                    SELECT value FROM 素数 WHERE value = (SELECT MAX(value) FROM 素数);
                """
            )
        subprocess.run("cls", shell=True)
        print(f"{pData[0][0]}")
        time.sleep(0.01)


if __name__ == "__main__":
    target = 2 ** 256
    dbFile = "prime_number.db"
    endFlag = Value('i', 0)
    proc = Process(target=disp, args=(endFlag, ))
    proc.start()

    with MySQLite(dbFile) as database:
        pData = database.send_sql(
            f"""
                SELECT value FROM 素数 ORDER BY value ASC;
            """
        )
    
    n = int(pData[-1][0])

    try:
        while n < target:
            flag = 0
            for p in pData:
                if p[0] ** 2 > n:
                    break

                elif (n % p[0]) == 0:
                    flag = 1
                    break
                
                
            if flag == 0:
                try:
                    with MySQLite(dbFile) as database:
                        database.send_sql(
                            f"""INSERT INTO 素数 (value) VALUES({int(n)})"""
                        )
                        pData = database.send_sql(
                            f"""
                                SELECT value FROM 素数 ORDER BY value ASC;
                            """
                        )
                except Exception as e:
                    print(e)
                    
            n += 2
            time.sleep(0.01)
            
    except Exception as e:
        print(e)
        with endFlag.get_lock():
            endFlag.value = 1
        proc.join()
