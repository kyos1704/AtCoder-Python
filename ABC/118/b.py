n, m = map(int, input().split())
A = []
for i in range(n):
    k, *a = map(int, input().split())
    A.append(a)

S = set(range(1, m + 1))
for a in A:
    S &= set(a)

print(len(S))