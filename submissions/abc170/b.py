x,y=map(int,input().split())
count=0
if (x == 1 and y==2) or (x == 1 and y==4):
  count+=1
else:  
  for i in range(x+1):
    if y == 2*i+4*(x-i):
      count+=1
    else:
      pass

if count>=1:
  print('Yes')
else:
  print('No')
