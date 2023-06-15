n=int(input())
m=n
for j in range(1,int(n**0.5)+1):
  x=n//j
  y=abs(x-j)+(n%j)
  m=min(m,y)
print(m)
