a,b,k=map(int,input().split())
if k-a>=0:
  k-=a
  a=0
  if b-k<=0:
    b=0
  else:
    b-=k   
else:
  a-=k
print(a,b)
