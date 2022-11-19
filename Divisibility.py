N = int(input())
arr = list(map(int, input().split()))
num = 0
for i in range(len(arr)):
    num =num*10+int(str(arr[i])[-1])
if num!=0 and num%10==0:
    print('Yes')
else:
    print('No')