n=input()
k=len(str(n))
count=0
for i in range(k):
  t=n[i]
  count +=int(t)
if count%9 == 0:
  print('Yes')
else:
  print('No')
