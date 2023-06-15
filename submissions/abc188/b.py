n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
k=0
for i in range(0,n):
  k+=(a[i]*b[i])
if k==0:
  print('Yes')
else:
  print('No')
