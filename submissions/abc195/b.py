a,b,w=map(int,input().split())
w*=1000
l=[]

if w%a==0:
  l+=[w//a]
else:
  for i in range(1,w//a):
    for j in range(a+1,b+1):
      if w==(j*i+a*(w//a-i)):
        l+=[w//a]

if w%b==0:
  l+=[w//b]
else:
  for i in range(w//b):
    for j in range(a,b):
      if w==j*i+b*(w//b+1-i):
        l+=[w//b+1]

if l==[]:
  print('UNSATISFIABLE')
else:
  print(min(l),max(l))
