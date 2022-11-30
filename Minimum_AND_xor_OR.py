for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    min = arr[0] ^ arr[1]
    for i in range(1, n - 1):
        temp = arr[i] ^ arr[i + 1]
        if temp < min:
            min = temp

    print(min)


# 2
# 5
# 1 2 3 4 5
# 3
# 2 4 7
#
# 1
# 3
