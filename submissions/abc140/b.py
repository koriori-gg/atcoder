n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=list(map(int,input().split()))
point=b[a[0]-1]
mae=0
for i in range(1,n):
  point+=b[a[i]-1]
  if (a[mae]+1==a[i]) and (a[i]!=1):   
    point+=c[a[i]-2]
  mae=i
print(point)
