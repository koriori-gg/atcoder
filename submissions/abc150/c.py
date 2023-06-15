import itertools
n=int(input())
p=list(map(int,input().split()))
q=list(map(int,input().split()))

list_dic=list(range(1,n+1))
p=tuple(p)
q=tuple(q)

seq=list((itertools.permutations(list_dic,n)))

print(abs(seq.index(p) - seq.index(q)))
