n, a, b, c, d = map(int, input().split())
s = list(str(input()))

a = a - 1
b = b - 1
c = c - 1
d = d - 1


def rec(s, a, b, c, d):
    #ss = s.copy()
    #ss[a] = 'A'
    #ss[b] = 'B'
    #print(str(ss),a,b,c,d)
    if a > c or b > d:
        return False
    if a == c and b == d:
        return True

    if a+1 < len(s) and s[a + 1] == '.' and a+1 != b:
        if rec(s, a + 1, b, c, d):
            return True
    if a+2 < len(s) and s[a + 2] == '.' and a + 2 != b:
        if rec(s, a + 2, b, c, d):
            return True
    if b + 1 < len(s) and s[b + 1] == '.' and b + 1 != a:
        if rec(s, a, b + 1, c, d):
            return True
    if b+2 < len(s) and s[b + 2] == '.' and b + 2 != a:
        if rec(s, a, b + 2, c, d):
            return True

    return False

result = rec(s, a, b, c, d)
if result:
    print("Yes")
else:
    print("No")
    