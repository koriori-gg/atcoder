a,b,c,d=map(int,input().split())
list=[]
list+=[a,b,c,d]
for i in range(0,3):
  if sum(list)-list[i]==list[i]:
    print('Yes')
    exit()
  else:
    pass
if sum(list)-list[0]-list[1]==list[0]+list[1]:
  print('Yes')
  exit()
elif sum(list)-list[0]-list[2]==list[0]+list[2]:
  print('Yes')
  exit()
elif sum(list)-list[0]-list[3]==list[0]+list[3]:
  print('Yes')
  exit()
elif sum(list)-list[1]-list[2]==list[1]+list[2]:
  print('Yes')
  exit()
elif sum(list)-list[1]-list[3]==list[1]+list[3]:
  print('Yes')
  exit()
elif sum(list)-list[2]-list[3]==list[2]+list[3]:
  print('Yes')
  exit()
else:
  print('No')
