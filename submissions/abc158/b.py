n,a,b=map(int,input().split())
k=n//(a+b)
j=n-(a+b)*k
if j==0:
  print(a*k)
else:
  if j>=a:
    print(a*(k+1))
  else:
    print(a*k+j)
