
import math

n, d = map(int, input().split())

X = [list(map(int, input().split())) for i in range(n)]


def Distance(a = [], b = []):
    res = 0.0
    for x, y in zip(a, b):
        res += (x - y) * (x - y)
    return math.sqrt(res)

count = 0
for i in range(int(len(X))):
    for j in range(i + 1, int(len(X))):
        r = Distance(a=X[i], b=X[j])
        if r.is_integer():
            count+=1
        

print(count)
