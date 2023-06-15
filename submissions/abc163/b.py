n,m=map(int,input().split())
a=list(map(int,input().split()))
b=sum(a)
if n-b>=0:
  print(n-b)
else:
  print(-1)
