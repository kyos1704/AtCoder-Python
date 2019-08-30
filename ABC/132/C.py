n = int(input())

d = [int(i) for i in input().split()]

d.sort()
num = int(len(d) / 2)
ans = d[num ] - d[num-1]
#print(d)
#print(d[num],d[num+1])
print(ans)