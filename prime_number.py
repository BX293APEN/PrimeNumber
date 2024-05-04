import subprocess, time
def init():
    with open("prime_number.list", "w", encoding="UTF-8") as pFile:
        pFile.write("2\n3")

def list_sort():
    with open("prime_number.list", "r", encoding="UTF-8") as pFile:
        pData = pFile.read().split("\n")
    pDataList = sorted(list(set(pData)), key = lambda value: int(value))
    data = "\n".join([i for i in pDataList])
    #print(data)
    with open("prime_number.list", "w", encoding="UTF-8") as pFile:
        pFile.write(data)

if __name__ == "__main__":
    list_sort()
    target = 2 ** 256
    with open("prime_number.list", "r", encoding="UTF-8") as pFile:
        pData = [int(i) for i in pFile.read().split("\n")]
    n = int(pData[-1])
    while n < target:
        subprocess.Popen("cls", shell=True)
        flag = 0
        print(f"{len(str(n))}桁")
        for p in pData:
            if (n % p) == 0:
                flag = 1
                break
        if flag == 0:
            pData.append(n)
            with open("prime_number.list", "a", encoding="UTF-8") as pFile:
                pFile.write(f"\n{n}")
        n += 2
        time.sleep(0.001)