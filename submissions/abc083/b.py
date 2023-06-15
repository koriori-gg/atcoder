n,a,b=map(int,input().split())
count=0
for i in range(1,n+1):
    result = sum(list(map(int,str(i))))
    if a<= result <=b:
      count+=i
print(count)
