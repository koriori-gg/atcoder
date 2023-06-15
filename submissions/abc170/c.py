x,n=map(int,input().split())
p=list(map(int,input().split()))
for i in range(0,100):
  if p.count(x-i)==0 and 0<=x-i<=100:
    print(x-i)
    exit()
  elif p.count(x+i)==0 and 0<=x-i<=100:
    print(x+i)
    exit()
