def rec(s):
    if not (s == "") and int(s) > n:
        return 0
    res = 0
    if all(c in s for c in '753'):
        res += 1
    for c in '753':
        res += rec(s + c)
    return res

n = int(input())
print(rec(""))