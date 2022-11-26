def delete(n,k,a):
	temp=[]
	for i in a:
		while k and temp and temp[-1]<i:
			temp.pop()
			k-=1
		temp.append(i)
	print(" ".join(map(str,temp)))

for i in range(int(input())):
	n,k=map(int,input().split())
	a=map(int,input().split())
	delete(n,k,a)