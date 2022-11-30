for _ in range(int(input())):
    n, k = map(int, input().split())
    a = input()
    max = ""
    p = -1
    for i in range(n):
        if max < a:
            max = a
            d = i
        elif max == a:
            p = i - d
            break
        a = a[1:] + a[:1]

    if p == -1:
        print(d + (k - 1) * n)
    else:
        print(d + (k - 1) * p)


# 2
# 5 2
# 10101
# 6 2
# 010101
# 9
# 3