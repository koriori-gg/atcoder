n=int(input())
xy=[list(map(int,input().split())) for _ in range(n)]
max=0
for i in range(n):
  for j in range(i,n):
    if max<(xy[i][0]-xy[j][0])**2 + (xy[i][1]-xy[j][1])**2:
      max=(xy[i][0]-xy[j][0])**2 + (xy[i][1]-xy[j][1])**2
max**=0.5
print('{:.4f}'.format(max))
