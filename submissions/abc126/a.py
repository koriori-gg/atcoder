n,k=map(int,input().split())
s=input()
a=s[k-1].lower()
print(s[:k-1]+a+s[k:])
