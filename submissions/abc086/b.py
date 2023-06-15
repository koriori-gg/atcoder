a,b=input().split()
c=int(a+b)
count=0
for i in range(1,100101):
  if c%i==0 and c/i==i:
    print('Yes')
    count+=1
    exit()
  else:
    pass
if count==0:
  print('No')
