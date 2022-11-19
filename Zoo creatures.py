def find_gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def find_lcm(a, b):
    return (a * b) // find_gcd(a, b)

t = int(input())
for _ in range(t):
    a,b = map(int, input().split())
    common = find_lcm(a,b)
    print(common//a,common//b)