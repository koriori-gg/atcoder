n=int(input())
h=list(map(int,input().split()))
m=0
count=0
list=[]
for i in range(n-1):
  if h[i]>=h[i+1]:
    count+=1
  else:
    if m<=count:
      m=count
    count=0

print(max(m,count))
