import sys

lt = 0 # line total
lc = 0 # line counter

def test(x, m):
    # a = (x - 1) % (m - 1) == 0
    b = (x * (x - 1)) % (m * (m - 1)) == 0
    return b

def solve(m):
    ret = []
    mx = m * (m - 1) # 1 < x < mx
    m1 = m - 1 # m=6, m1 = 5
    print("mx:", mx)
    print("m1:", m1)

    x = 0 #current m to test out
    while True:
        x += m1

        if x >= mx:
            break

        # print("x:", x)
        if(test(x + 1, m)):
            ret.append(x + 1)

    return ret

for i in sys.stdin:
    i = i.strip("\n")

    lc += 1

    if lc == 1:
        lt = int(i)
        continue
    
    i = int(i)
    ret = solve(i)
    for e in ret:
        print(e, end=' ')

    print("")
