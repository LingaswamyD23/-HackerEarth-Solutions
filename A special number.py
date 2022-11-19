def sumDigit(num):
    return sum(list(map(int, num.strip())))

T = int(input())
for _ in range(T):
    n = a = int(input())
    while True:
        if sumDigit(str(n)) %4 == 0:
            print(n)
            break
        n +=1