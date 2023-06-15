import math
n=int(input())
t=[int(input()) for _ in range(n)]
max=max(t)
for i in range(n):
  max=max * t[i] // math.gcd(max,t[i])
print(max)
