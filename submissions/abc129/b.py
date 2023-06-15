n=int(input())
w=list(map(int,input().split()))
c=10**6
for i in range(1,n):
  a=sum(w[0:i])
  b=sum(w[i:])
  if c>abs(a-b):
    c=abs(a-b)
print(c)
