def check_prime(num):
    i = 2
    while i * i <= num:
        if num % i == 0:
            return False
        i += 1
    return True


for _ in range(int(input())):
    N = int(input())
    if N == 1:
        print("YES")
    elif N == 2:
        print("NO")
    elif check_prime(N + 1):
        print("NO")
    else:
        print("YES")

