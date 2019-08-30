
#readed editional
MOD = int(1e9)+7
#print(MOD)
S = [int(x) if x != '?' else - 1 for x in input()]

n = len(S)

dp = [[0]*13 for i in range(n+1)]

dp[0][0] = 1
#print(dp)

for i in range(n):
    c = S[i]
    if c == -1:
        for j in range(10):
            for ki in range(13):
                dp[i + 1][(ki * 10 + j) % 13] += dp[i][ki]
    else:
        for ki in range(13):
            dp[i + 1][(ki * 10 + c) % 13] += dp[i][ki]        
    for j in range(13):
        dp[i+1][j] %= MOD

#print(S)
#print(dp)
print(dp[len(dp)-1][5])
