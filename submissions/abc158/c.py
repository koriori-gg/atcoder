a,b=map(int,input().split())
for i in range(10001):
  if i*0.08//1 == a and i*0.1//1 == b:
    print(i)
    exit()
else:
  print(-1)
