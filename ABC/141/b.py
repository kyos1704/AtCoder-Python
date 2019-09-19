s = list(input())

a = ['R', 'U', 'D']
b = ['L', 'U', 'D']

def solve(s):
    for i in range(len(s)):
        if i % 2 == 0:
            if (s[i] not in a):
                return False
        else:
            if (s[i] not in b):
                return False
    return True

if (solve(s)):
    print("Yes")
else:
    print("No")