n = int(input())


dp = [-1 for _ in range(90)]

def rec(n):
    if dp[n] != -1:
        return dp[n]
    if n == 0:
        dp[n] = 2
    elif n == 1:
        dp[n] = 1
    else:
        dp[n] = rec(n - 1) + rec(n - 2)
    return dp[n]

print(rec(n))