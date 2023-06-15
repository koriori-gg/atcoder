from math import gcd
k=int(input())
r=range(1,k+1)
s=sum((gcd(gcd(a,b),c)) for a in r for b in r for c in r)
print(s)
