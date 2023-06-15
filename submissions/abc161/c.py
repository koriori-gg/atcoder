n,k=map(int,input().split())
if n%k==0:
  print(0)
else:
  print(min(n,abs(k-n%k)))
