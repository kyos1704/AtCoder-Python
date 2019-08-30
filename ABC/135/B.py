import numpy as np
n = int(input())
p = list(map(int, input().split()))

p2 = p.copy()
p2.sort()

p = np.asarray(p)
p2 = np.asarray(p2)
p3 = [p!=p2]
c = np.count_nonzero(p3)
if c == 2 or c == 0:
    print("YES")
else:
    print("NO")
