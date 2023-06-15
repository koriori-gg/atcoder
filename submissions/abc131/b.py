n,l=map(int,input().split())
a=[]
for i in range(1,n+1):
  a+=[l+i-1]
b=sum(a)
c=10**9
for j in range(n):
  if abs(c)>abs(a[j]):
    c=a[j]
print(b-c)
