n=int(input())
a=list(map(int,input().split()))
l=len(a)
b=list(set(a))
l2=len(b)
if l == l2:
  print('YES')
else:
  print('NO')
