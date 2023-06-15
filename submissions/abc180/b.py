n=int(input())
x=list(map(int,input().split()))
md=0
yd=0
cd=0
for i in range(n):
  y=abs(x[i])
  yd+=x[i]**2
  md+=y
  if  cd < y:
    cd = y
  else:
    pass
print(md)
print(f'{(yd**0.5):.09f}')
print(cd)
    
  
  
