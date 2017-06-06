import sys

while True :
    line = sys.stdin.readline().strip()
    if line == "":
        break
    else :
        a,b = line.split(" ")
        print str(int(a)+int(b))
        
