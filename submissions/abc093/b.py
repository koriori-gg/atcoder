a,b,k=map(int,input().split())
if b-a>=k:
  l1=[int(i) for i in range(a,a+k)]
  l2=[int(b-j) for j in range(k)]
else:
  newk=b-a
  l1=[int(i) for i in range(a,a+newk+1)]
  l2=[int(b-j) for j in range(newk+1)]

l=l1+l2
l=list(set(l))
l.sort()
for i in range(len(l)):
  print(l[i])
