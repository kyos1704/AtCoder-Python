n, a, b, c, d = map(int, input().split())

s = input()
s = '#' +s

def check(s, a, b):
    return not "##" in s[a:b]


def solve(s,a,b,c,d):
    can_swap = "..." in s[b - 1:d + 2]
    can_reach_each = check(s, a, c) and check(s, b, d)
    if not can_reach_each:
        return False
    if (a < b and c < d) or (b < a and d < c):
        return True
    else:
        if can_swap:
            return True
        else:
            return False

if solve(s, a, b, c, d):
    print("Yes")
else:
    print("No")

