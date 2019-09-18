n = int(input())

h = list(map(int, input().split()))


count = 0
max_count = 0

for i in range(1, len(h)):
    if (h[i - 1] >= h[i]):
        count += 1
    else:
        max_count = max(count, max_count)
        count = 0

max_count = max(count, max_count)
count = 0
print(max_count)
