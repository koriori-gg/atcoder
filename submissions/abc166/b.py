n,k=map(int,input().split())
d=[]*k
a=[]*k
for i in range(k):
  d+=[int(input())]
  a+=set((map(int,input().split())))
a=set(a)         
list_obake=set(range(1,n+1))
b=list(list_obake-a)
print(len(b))
