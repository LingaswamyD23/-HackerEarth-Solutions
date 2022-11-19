s = input()
for ch in s:
    s1 = ''
    
    if ch.isupper():
        s1 +=ch.lower()
    else:
        s1 +=ch.upper()
    print(s1)#print(s.caseswap())