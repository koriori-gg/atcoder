h,n=map(int,input().split())
a=list(map(int,input().split()))
a.sort()
kougeki=0
for i in range(n):
  kougeki+=a[i]
if h>kougeki:
  print('No')
else:
  print('Yes')
  
