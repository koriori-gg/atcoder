n=int(input())
ab= [map(int, input().split()) for _ in range(n)]
a, b = [list(i) for i in zip(*ab)]
k=0
l=0
w=0
newa=sorted(a, reverse=True)
newb=sorted(b, reverse=True)

if newa[-1]==newa[-2] or newb[-1]==newb[-2]:
  k=newa[-1]
  l=newb[-1]
  print(max(k,l))
elif a.index(newa[-1])==b.index(newb[-1]):
  k=newa[-1]+newb[-1]
  l=newb[-2]
  w=newa[-2]
  print(min(k,w,l))
else:
  l=newb[-1]
  w=newa[-1]
  print(max(l,w))
