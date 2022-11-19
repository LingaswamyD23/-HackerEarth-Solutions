T = int(input())
while T>0:
    x,y,a,b = map(int, input().split())
    if (x*y) == (a+b):
        print('Yes')
    else:
        print('No')
    T -=1