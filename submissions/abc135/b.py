n=int(input())
a=list(map(int,input().split()))
b=sorted(a)
count=0
for i in range(n):
  if a[i] != b[i]:
    count+=1
if count==0 or count==2:
  print('YES')
else:
  print('NO')
