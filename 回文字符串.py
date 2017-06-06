import sys
import copy

while True:
    str1 = sys.stdin.readline().strip()

    if str1 == "" :
        break
    else :
        ls = list(str1)
        ls1 = copy.deepcopy(ls)

        ls.reverse()
        if cmp(ls,ls1) == 0 :
            print "Yes!"
        else :
            print "No!"
            
