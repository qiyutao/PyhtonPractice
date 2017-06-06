import sys

while True:
    str1 = sys.stdin.readline().strip()

    if str1 == "" :
        break
    else :
        ls = list(str1)
        dt = []
        dt_ls = []
        for i in range(0, str1.__len__()) :
            ls1 = []
            if ls.count(str1[i]) > 1 :
                if str1[i] in dt :
                    dt_ls[dt.index(str1[i])].append(i)
                else :
                    ls1.append(i)
                    dt_ls.append(ls1)
                    dt.append(str1[i])


        for k in range(0,dt_ls.__len__()) :
            for j in range(0,dt_ls[k].__len__()-1):
                sys.stdout.write(dt[k]+":" + str(dt_ls[k][j]) + ",")
            print dt[k] + ":" + str(dt_ls[k][-1])

