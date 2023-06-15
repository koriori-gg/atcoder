k=int(input())
a,b=map(int,input().split())
c=k
while c<=b:
  if a<=c<=b:
    print('OK')
    exit()
  c+=k
print('NG')
