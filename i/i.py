import sys

dict = {}
lc = 0 # line counter
lt = 0 # total line

for i in sys.stdin:
    lc += 1

    if lc == 1:
        lt = int(i)
        continue


    i = i.strip("\n")
    v = i.split(" ")

    a = v[0]
    b = v[1]

    dict[a] = b

    if lc >= lt + 1:
        break

print(dict)


# for each key in dict, print the value
for k in dict:
    v = dict[k]
    print("entry", k, v)

    while v in dict:
        v = dict[v]
        dict[k] = v
        print(dict)
        print("sub-entry", k, v)

    print(k, v)
