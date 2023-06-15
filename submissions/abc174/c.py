k=int(input())
x=0
for i in range(1,10**7):
  x*=10
  x+=7
  x%=k
  if x==0:
    print(i)
    exit()
else:
  print(-1)
