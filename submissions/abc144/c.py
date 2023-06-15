n=int(input())
min=n-1
for i in range(2,int(n**0.5 + 1)):
  if n%i==0:
    if min>i - 2 +  n//i:
      min=i -2  + n//i
print(min)
