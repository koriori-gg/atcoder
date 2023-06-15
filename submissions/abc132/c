n=int(input())
d=list(map(int,input().split()))
d.sort()
if len(d)%2==0:
  if d[n//2-1]==d[n//2]:
    print(0)
  else:
    print(d[n//2]-d[n//2-1])
else:
  if d[n//2+1]==d[n//2] or d[n//2+1]==d[n//2+2]:
    print(0)
  else:
    print(d[n//2+2]-d[n//2])
