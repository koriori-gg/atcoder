a,b=input().split()
lista=[]
listb=[]
for i in range(3):
  lista+=[int(a[i])]
  listb+=[int(b[i])]
print(max(sum(lista),sum(listb)))
