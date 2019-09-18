A, B = map(int, input().split())

first = 1

ans = 0
count = 1

while (True):
    if count >= B:
        break
    else:
        count -= 1
        count += A
        ans += 1

print(ans)