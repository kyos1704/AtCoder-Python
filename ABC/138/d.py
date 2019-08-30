import sys
input = sys.stdin.readline
sys.setrecursionlimit(900000)

n, q = map(int, input().split())

#print(n,q)
edge = []
for i in range(n-1):
    a = list(map(int, input().split()))
    edge.append(a)

add_list = []
for i in range(q):
    p = list(map(int, input().split()))
    add_list.append(p)

#print(edge,add_list)


dir_edge = [[] for i in range(n)]

for e in edge:
    dir_edge[e[0]-1].append(e[1]-1)
    dir_edge[e[1]-1].append(e[0]-1)
#print(dir_edge)


ans = [0]*n
for v in add_list:
    ans[v[0]-1] += v[1]
#print(add_value)


def dfs(index, parent):
    if parent != -1:
        ans[index] += ans[parent]
    for i in dir_edge[index]:
        if (parent != i):
            dfs(i,index)

dfs(0, -1)
print(*ans)
