def printMaxNumber(n):
    if n % 2 == 0:
        print("1" * (n // 2))
    elif n % 2 != 0:
        a = int(n - 3) // 2
        print("7" + ("1") * a)



T = int(input())
if 1<=T<=100:
    num_dict = {0:6, 1:2, 2:5, 3:5, 4:4, 5:5, 6:6, 7:3, 8:7, 9:6}
    for _ in range(T):
        N = input()
        total = 0
        for num in N:
            total += num_dict[int(num)]
        printMaxNumber(total)
