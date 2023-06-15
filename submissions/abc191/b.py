n,x=map(int,input().split())
a=list(map(int,input().split()))
dash=[]
for i in range(n):
  if a[i]!=x:
    dash+=[a[i]]
print(*dash)
