n=int(input())
a=list(map(int,input().split()))
a.sort(reverse=True)
b=a[::2]
print(2*sum(b)-sum(a))
