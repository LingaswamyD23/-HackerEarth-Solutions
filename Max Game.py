import math
def solve (N):
    # Write your code here
   k = int(math.log2(N))
   if (pow(2,k)<=N):
       return int(pow(2,k))

T = int(input())
for _ in range(T):
    N = int(input())

    out_ = solve(N)
    print (out_)