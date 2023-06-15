x=int(input())
count=0
while x>0:
  for i in range(2,int(x**0.5)+1):
    if x%i != 0:
      count+=1
  if count==int(x**0.5)-1:
    print(x)
    exit()
  x+=1
  count=0
