import math
c=int(input())
l=set()
count=0

for i in range(2,int(c**0.5)+1):
  if c>=i**2:
    count=i
  else:
    break

d=0
for i in range(2,count+1):
  d=int(math.log(c, i))
  for j in range(2,d+1):
    l.add(i**j)

print(c-len(l))
