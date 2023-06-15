n,x=map(int,input().split())
l=list(map(int,input().split()))
a=0
count=0

if a<=x:
  count+=1
for i in range(n):
  a+=l[i]
  if a<=x:
    count+=1
print(count)
