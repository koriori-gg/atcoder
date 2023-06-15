n=int(input())
v=list(map(int,input().split()))
v.sort()
k=v[0]
for i in range(1,n):
  k=(k+v[i])/2
print(k)
