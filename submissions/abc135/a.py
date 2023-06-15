a,b=map(int,input().split())
if a%2==0:
  if b%2!=0:
    print('IMPOSSIBLE')
    exit()
elif a%2!=0:
  if b%2==0:
    print('IMPOSSIBLE')
    exit()
print((a+b)//2)
