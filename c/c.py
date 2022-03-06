import sys


count = 1
for string in sys.stdin:
    if count % 2 == 1:
        n = int(string)
        count += 1
        continue
    nums = list(map(int, string.split()))
    flag = False
    for i in range((n // 2)):
        k = i + 1
        flag = True
        for j in range(k, n + 1, k):
            if j - 1 + k < n and nums[j - 1] >= nums[j - 1 + k]:
                flag = False
        if flag == True:
            print(k)
            break

    if not flag:
        print("ABORT!")

    count += 1
