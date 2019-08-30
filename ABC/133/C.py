L, R = map(int, input().split())

import math

#L<=i<j<=R
# i*j mod 2019の最小値

if R - L > 2030:
    L = 0
    R = 2019

result = 2019
for i in range(L, R+1):
    for j in range(i+1, R+1):
        tmp = (i * j) % 2019
        result = min(tmp, result)
        
print(result)