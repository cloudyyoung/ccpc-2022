import sys
import math

from numpy import power

# Integer to binary array
def i2b(x):
    return [int(i) for i in bin(x)[2:]]



for i in sys.stdin:
    c = int(i)
    d = math.ceil(math.log2(c)) # number of coins
    e = math.ceil(math.pow(2, d)) # number of combiantions

    print("citizens:", c, "| coins:", d, "| combinations:", e)

    if c <= 2:
        print(1)
        break

    # Find binary of c
    c_prev = i2b(c - 1)
    c_b = i2b(c)
    c_next = i2b(c + 1)
    print(c_prev, c_b)


    f_n = [] # Number of occurence for nth coin to be flipped
    for i in range(0, d):
        if i == 0:
            f_n.append(0)
        else:
            f_n.append(pow(2, d - i - 1))

    # If the second last digit is the same, then falls into "1/e" flips until the last coin
    if c_b[-2] == c_prev[-2]:
        f_n[d - 1] = 1
    else:
        f_n[d - 1] = 0
    
    print(f_n)

    f_n_Ex = 0
    t = 0
    for i in range(1, d):
        nth_coin =  i + 1
        comb = f_n[i]

        # Last one, say comb + c
        if i == d - 1:
            comb += c
        else:
            t += comb

        nth_prob = comb / e
        Ex = nth_prob * nth_coin
        print("nth_coin:", nth_coin, "| comb:", comb, "| prob:", nth_prob, "| Ex:", Ex)
        f_n_Ex += Ex

    print("t", t)
    print("f_n:", f_n)
    print("f_n_Ex:", f_n_Ex)

    
    f_no_flip_prob = c / e
    print("f_no_flip_prob:", f_no_flip_prob)

    f_prob = (1 / f_no_flip_prob) * f_n_Ex
    print("f_prob:", f_prob)


    break
