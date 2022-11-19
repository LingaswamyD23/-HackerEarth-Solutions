n = int(input())
s = input()
if s.find("HH") == -1:
    print("YES")
    print(s.replace(".", "B"))
else:
    print("NO")
