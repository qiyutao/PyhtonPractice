import math
import sys

while True:
    n = sys.stdin.readline().strip()
    if n == "":
        break
    else :
        n = int(n)
        i = 1
        y1 = 0
        y2 = 0
        while i<=n:
            if i%2 != 0:
                y1 += math.factorial(i)
            else:
                y2 += math.factorial(i)
            i += 1
        print str(y1)+" "+str(y2)
