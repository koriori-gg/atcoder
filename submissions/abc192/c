n,k=map(int,input().split())
for i in range(k):
  list_cap=list(str(n))
  list_cap.sort(reverse=True)
  l=len(list_cap)
  n=0
  for i in range(l):
    d=int(list_cap[i])
    n+=(d*10**(l-i-1) - d*10**(i))
print(n)
