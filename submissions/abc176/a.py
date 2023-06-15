n,x,t = map(int,input().split())
k = n//x
if n%x==0:
  print(k*t)
else:
  print((k+1)*t)
