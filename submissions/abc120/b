a,b,k=map(int,input().split())
lista=[]
listb=[]

for j in range(1,int(a**0.5)+1):
  if a%j==0 and a//j!=j:
    lista+=[j]
    lista+=[a//j]
  elif a%j==0 and a//j==j:
    lista+=[j]

for j in range(1,int(b**0.5)+1):
  if b%j==0 and b//j!=j:
    listb+=[j]
    listb+=[b//j]
  elif b%j==0 and b//j==j:
    listb+=[j]
newlist=list(set(listb)&set(lista))
newlist.sort()
print(newlist[-k])
