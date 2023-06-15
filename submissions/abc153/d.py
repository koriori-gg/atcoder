h=int(input())
monster=1
i=1
while h>1:
  if h!=1:
    h=h//2
    monster+=2*i
    i*=2
print(monster)
