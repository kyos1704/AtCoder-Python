n = int(input())

p = list(int(i) for i in input().split())


ans = 0
for i in range(1, n - 1):
    l = [p[i - 1], p[i], p[i + 1]]
    l.sort()
    if (l[1] == p[i]):
        ans += 1

print(ans)