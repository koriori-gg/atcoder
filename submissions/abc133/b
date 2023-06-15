n,d=map(int,input().split())
x=[list(map(int, input().split())) for _ in range(n)]
count=0

for i in range(n-1):
  for j in range(i,n):
    s=0
    for k in range(d):
      s+=(x[i][k] -x[j][k])**2
    s**=0.5
    if s==0:
      pass
    elif s == (s//1):
      count+=1
print(count)
