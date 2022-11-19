L = int(input())
N = int(input())
for _ in range(N):
    W, H = map(int, input().split())
    if W<L or H<L:
        print("UPLOAD ANOTHER")
    elif (W>=L and H>=L):
        if W !=H:
            print("CROP IT")
        else:
            print("ACCEPTED")
