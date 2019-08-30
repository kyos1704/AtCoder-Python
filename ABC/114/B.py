S = str(input())
data = [int(S[i:i+3]) for i in range(0,len(S)-2)]
#print(data)


ans = 787
import math
for i in data:
    tmp = abs(i-753)
    ans = min(ans, tmp)
    
print(ans)
