n=int(input())
m=int(n**(0.5))
list=[]
for i in range(1,m+1):
  if n%i == 0:
    list.append(i)
    if i != n//i:
      list.append(n//i)
list.sort()
for j in range(len(list)):
  print(list[j])
