prev = []
n = int(input())
for i in range(n):
    curr = input()
    prev.append(curr)
    count = 0
    for val in prev:
        if val < curr:
            count += 1

    print(count)