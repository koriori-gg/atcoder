n=int(input())
num=0
if n%2==0:
  num=(1/2)
else:
  num=(((n-1)/2)+1)/n
print('{:.07f}'.format(num))
