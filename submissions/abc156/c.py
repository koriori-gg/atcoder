n = int(input())
x = list(map(int, input().split()))
a = round(sum(x) / n)
y = 0
for i in range(0, n):
    y += (x[i] - a) ** 2
print(y)
