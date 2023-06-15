import math

l=int(input())
def comb(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))
base = comb(l-1,l-12)

if l==12:
  print(1)
else:
  print(base)
