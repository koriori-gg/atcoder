n=int(input())
a=list(map(int,input().split()))
b=max(a[0:2**(n-1)])
c=max(a[2**(n-1):])
print(a.index(min(b,c))+1)
