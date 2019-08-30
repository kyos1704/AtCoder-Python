n = int(input())

A = list(map(int, input().split()))

ans = []
for i in range(n):
    tmp = A[i]
    for j in range(1,n):
        if (j % 2 == 0):
            tmp += A[(i + j) % n]
        else:
            tmp -= A[(i + j) % n]
        print(i ,j,tmp)
    ans.append(tmp)
print(ans)

