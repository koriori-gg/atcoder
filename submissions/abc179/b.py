N=int(input())
z=0

for _ in range(N):
  a,b=map(int,input().split())
  if a==b:
    z+=1
    if z>=3:
      print('Yes')
      break
  else:
    z=0
  
else:
  print('No')
