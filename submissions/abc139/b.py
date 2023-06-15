a,b=map(int,input().split())
pocket=1
count=0
k=a-1
while pocket<b:
  pocket+=k
  count+=1
print(count)
