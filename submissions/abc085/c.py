n,y=map(int,input().split())
count=0
if y > n*10000 or y<n*1000 or y%1000!=0:
  print('-1 -1 -1')
  count+=1
  exit()
elif y == n*10000:
  print(n,'0 0')
  count+=1
  exit()
else:
  pass
for i in range(n+1):
  for j in range(n+1):
    if 10000*i+5000*j+1000*(n-i-j) == y and n-i-j>=0:
      print(i,j,n-i-j)
      count+=1
      exit()
if count==0:
  print('-1 -1 -1')
