import sys

while True :
    num = sys.stdin.readline().strip()
    if num == "":
        break
    else :
        ls = []
        for i in range(0,int(num)):
            tmp = input()
            ls.append(tmp)
        ls.sort()
        for i in ls:
            print  str(i)
