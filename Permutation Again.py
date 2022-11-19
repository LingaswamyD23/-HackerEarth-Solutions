maxnum = pow(10, 5) + 1
ansArr = [0,1,1]
for j in range(3, maxnum):
    if j % 2 == 0:
        mplier = j // 2
        ansArr += [mplier * j - 1]
    else:
        mplier = j // 2
        addition = j // 2 - 1
        ansArr += [mplier * j + addition]

T = int(input())

for _ in range(T):
    N = int(input())
    if N == 1:
        print(1)
    else:
        print(ansArr[N])