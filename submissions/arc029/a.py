n=int(input())
t=[int(input()) for _ in range(n)]
total1=0
total2=0
newlist=sorted(t, reverse=True)
for i in range(n):
  if total1 <= total2:
    total1+=newlist[i]
  else:
    total2+=newlist[i]
print(max(total1,total2))  
