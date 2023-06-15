s,t=input().split()
a,b=map(int,input().split())
u=input()
if s==u:
  print(int(a-1),' ',b)
elif t==u:
  print(a,' ',int(b-1))
else:
  print(a,' ',b)
