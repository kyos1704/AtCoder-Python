S = list(input())


zero = 0
one = 0
for i in S:
    if i == '0':
        zero += 1
    if i == '1':
        one += 1

ans = min(zero, one) * 2
print(ans)