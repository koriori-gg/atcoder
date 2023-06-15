n,m=map(int,input().split())
sc=[list(map(int,input().split())) for _ in range(m)]
k=0
if n==1:
  for i in range(10):
    k=str(i)
    for j in range(m):
      if int(k[sc[j][0]-1]) != sc[j][1]:
        break
    else:
      print(i)
      exit()
  else:
    print(-1)
else:
  for i in range(10**(n-1),10**n):
    k=str(i)
    for j in range(m):
      if int(k[sc[j][0]-1]) != sc[j][1]:
        break
    else:
      print(i)
      exit()
  else:
    print(-1)
