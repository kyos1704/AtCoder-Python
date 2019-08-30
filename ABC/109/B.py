def solve():
    n = int(input())

    W = []
    for i in range(n):
        tmp = list(input())
        W.append(tmp)

    c = ""
    for w in W:
        if W.count(w) > 1:
            return False

    for w in W:
        cc = w[len(w) - 1]
        if c == "" or c == w[0]:
            c = cc
        else:
            return False
    
    return True

if solve():
    print("Yes")
else:
    print("No")
    