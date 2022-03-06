import sys
lc = 0

a = '!'
b = 'a'

for i in sys.stdin:
    lc += 1

    if lc == 1:
        i = i.strip("\n")
        v = i.split(" ")
        a = v[0]
        b = v[1]

    if lc == 2:
        i = i.strip("\n")
        c = i.split(" ")
        
        # for each in c
        for e in c:
            if e == '<':
                print(",", end='')
                continue
            elif e == '>':
                print(".", end='')
                continue


            print("e: ", e, " | a: ", a, " | b: ", b)
            if e == a:
                print(b, end='')
            else:
                d = ord(e) - ord(a)
                print(chr(d + ord(b)), end='')
        break
