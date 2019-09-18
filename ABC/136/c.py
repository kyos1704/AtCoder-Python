n = int(input())
h = list(map(int, input().split()))


h[0] = h[0] - 1
for i in range(1, n):
    if(h[i-1] < h[i]):
        h[i] = h[i]-1

flag = True
for i in range(1, n):
    if(h[i-1] > h[i]):
        flag = False

if(flag):
    print("Yes")
else:
    print("No")
