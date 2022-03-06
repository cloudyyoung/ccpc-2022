
import sys

for i in sys.stdin:

    counter = 0
    j2 = i[0]


    # For each character in i
    for j in i:
        if j == j2:
            counter += 1
        else:
            print(str(counter) + j2, end='')
            counter = 1
            j2 = j

    print("")

    if i == '\n':
        break
