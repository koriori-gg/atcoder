n,x=map(int,input().split())
m=[int(input()) for _ in range(n)]
s=sum(m)
small=min(m)
ans1=(x-s)//small
ans2=len(m)
print(ans1+ans2)
