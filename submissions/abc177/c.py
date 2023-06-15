n=int(input())
a=list(map(int,input().split()))
ans=0
z=sum(a)
mod=10**9+7
for i in a:
  z-=i
  ans+=i*z
  ans%=mod
print(ans)
