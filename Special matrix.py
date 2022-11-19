import math

def prime_factors(num):
    # Using the while loop, we will print the number of two's that divide n
    facts = []
    while num % 2 == 0:
        facts.append(2)
        num = num / 2

    for i in range(3, int(math.sqrt(num)) + 1, 2):

        # while i divides n , print i ad divide n
        while num % i == 0:
            facts.append(i)
            num = num / i
    if num > 2:
        facts.append(num)
    return len(set(facts))




T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    prime_dict = {i: prime_factors(i) for i in range(2, (M + N) + 1)}
    sums = 0
    for row in range(1,N+1):
        for col in range(1,M+1):
            sums +=prime_dict[row+col]
    print(sums)
