a,b,c,k=map(int,input().split())
if k < a:
  print(k)
else:
  if k < a + b:
    print(a)
  else:
    print(a+(-1)*(k-a-b))
