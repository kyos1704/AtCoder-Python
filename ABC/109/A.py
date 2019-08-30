a,b = map(int,input().split())

def solve(a,b):
    for c in range(1, 3):
        if (a * b * c) % 2 == 1:
            return True
        else:
            return False

if (solve(a, b)):
    print("Yes")
else:
    print("No")