import sys

while True :
    line = sys.stdin.readline().strip()
    if line == "":
        break
    else :
        num = int(line)
        a,b = 1,1
        for i in range(2,num+1) :
            tmp = b
            b += a
            a = tmp
        print str(b)
