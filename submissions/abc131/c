import math
a,b,c,d=map(int,input().split())
base=b-a+1
#c
if a%c==0:
  minc=a//c
else:
  minc=a//c+1

if b%c==0:
  maxc=b//c
else:
  maxc=b//c
#d
if a%d==0:
  mind=a//d
else:
  mind=a//d+1

if b%d==0:
  maxd=b//d
else:
  maxd=b//d
#c*d
x= int(c*d  / math.gcd(c,d))
if a%x==0:
  minx=a//x
else:
  minx=a//x+1

if b%x==0:
  maxx=b//x
else:
  maxx=b//x
print(base-((maxc-minc+1)+(maxd-mind+1)-(maxx-minx+1)))
