n,m=map(int,input().split())
a=list(map(int,input().split()))
a.sort(reverse=True)
sum_a=sum(a)
count=0
for i in range(m):
  if a[i] >= sum_a/(4*m):
    count+=1
  else:
    print('No')
    break
if count == m:
  print('Yes')
  exit()
