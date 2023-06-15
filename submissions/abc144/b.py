n=int(input())
z=0
for i in range(1,10):
  if n % i == 0:
    k = int(n / i)
    if 1 <= k <= 9:
      z+=1
if z>=1:
  print('Yes')
else:
  print('No')
