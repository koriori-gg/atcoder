n,m=map(int,input().split())
for i in range(2):
  for j in range(m//4+1):
    if i + 2*j == m-2*n and n -i -j >= 0:
      print(n-i-j,i,j)
      exit()
else:
  print(-1,-1,-1)
