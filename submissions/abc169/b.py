n=int(input())
a=list(map(int,input().split()))
ans = 1
for x in range(n):
  if a[x] == 0:
    print(0)
    exit()
  else:
    pass
for i in range(n):
  ans*=a[i]
  if ans >10**18:
    print(-1)
    exit()
print(ans)
