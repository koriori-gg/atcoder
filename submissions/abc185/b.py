n,m,t=map(int,input().split())
ab = [map(int, input().split()) for _ in range(m)]
a, b = [list(i) for i in zip(*ab)]
#初期値
n1=n-(a[0])
if n1<=0:
  print('No')
  exit()
#循環
for j in range(0,m-1):
  n1+=(b[j]-a[j])
  if n1>n:
    n1=n
  n1-=(a[j+1]-b[j])
  if n1<=0:
    print('No')
    exit()
#mかいめ
n1+=(b[m-1]-a[m-1])
if n1>n:
  n1=n
#last
if n1-(t-b[m-1]) > 0:
  print('Yes')
else:
  print('No')
