n,k=map(int,input().split())
h=list(map(int,input().split()))
h.sort()
if n<=k:
  print(0)
else:
  h=h[0:n-k]
  print(sum(h))
