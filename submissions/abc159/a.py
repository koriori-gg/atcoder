n,m=map(int,input().split())
count=0
if n>=2:
  count+=n*(n-1)//2
if m>=2:
  count+=m*(m-1)//2
print(count)
