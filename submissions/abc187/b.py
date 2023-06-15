n=int(input())
xy=[map(int,input().split()) for _ in range(n)]
x,y=[list(k) for k in zip(*xy)]
count=0
for j in range(1,n):
  for i in range(j):
    if -1<=(y[j]-y[i])/(x[j]-x[i])<=1:
      count+=1
print(count)
