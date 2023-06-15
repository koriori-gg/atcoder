n = int(input())
k = n//1000
if n % 1000 == 0:
  print(0)
else:
  print(1000*(k+1)-n)
