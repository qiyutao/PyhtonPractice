import sys
number = []
while True:
    line  = sys.stdin.readline().strip()
    if line == "":
        break
    else:
        number.append(line)

for i in range(0,number.__len__()):
    oct = ""
    stack = []
    num = int(number[i])
    while num>=8:
        stack.append(str(num%8))
        num /= 8
    stack.append(num)
    for j in range(0,stack.__len__()):
        oct += str(stack.pop())
    print(oct)
