n = int(input())

A = list(map(int, input().split()))
B = list(map(int, input().split()))
A2 = A.copy()

for i in range(n):
    if A[i] > B[i]:
        A[i] = A[i] - B[i]
    else:
        A[i + 1] = max(0, A[i + 1] - (B[i] - A[i]))
        A[i] = 0
        

    #print(A)

ans = 0
for i in range(n + 1):
    ans = ans + (A2[i] - A[i])
    #print(ans)
    
print(ans)
