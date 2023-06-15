n=int(input())
a=list(map(int,input().split()))
b=0
for i in range(n-1):
  if a[i] >a[i+1]:
    b+=a[i] - a[i+1]
    a[i+1]=a[i]
print(b)
