n,m=map(int,input().split())
ab = [map(int, input().split()) for _ in range(m)]
a, b = [list(i) for i in zip(*ab)]
k=int(input())
cd = [map(int, input().split()) for _ in range(k)]
c, d = [list(i) for i in zip(*cd)]

max=0
for i in range(2**k):
  bag=set()
  total=0
  for j in range(k):
    if ((i>>j)&1):
      bag.add(c[k-1-j])
    else:
      bag.add(d[k-1-j])
  for l in range(m):
    if (a[l] in bag) and (b[l] in bag):
      total+=1
  if max<total:
    max=total
print(max)
