n,k,q=map(int,input().split())
mylist=[k-q for _ in range(n)]
a=[int(input()) for _ in range(q)]
for i in range(q):
  mylist[a[i]-1]+=1
for j in range(n):
  if mylist[j]>0:
    print('Yes')
  else:
    print('No')
