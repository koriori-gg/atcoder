n, x = map(int,input().split())
x*=100
for i in range(n):
  v, p = map(int, input().split())
  x -= p * v
  if x < 0:
    print(i + 1)
    exit()
else:
  print(-1)    
