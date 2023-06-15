n=int(input())
a=list(map(int,input().split()))

i=0
number=1
while i<n:
  if a[i]==number:
    number+=1
  i+=1
if number == 1:
  print(-1)
elif n == (number-1):
  print(0)
else:
  print(n-(number-1))
