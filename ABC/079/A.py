n = list(str(input()))

def ans(n):
    for i in range(len(n) - 2):
        if n[i] == n[i + 1] and n[i + 1] == n[i + 2]:
            return True
    return False

if ans(n):
    print("Yes")
else:
    print("No")