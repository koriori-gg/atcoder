k,n=map(int,input().split())
a=list(map(int,input().split()))
max=0
for i in range(n-1):
  if a[i+1]-a[i]>max:
    max=a[i+1]-a[i]
if k-a[n-1]+a[0] > max:
  max=k-a[n-1]+a[0]
print(k-max)
