
def fib(n):
    fibtable = [0, 1]
    for i in range(2, n+1):
        fibtable.append(fibtable[i-1] + fibtable[i-2])
    return fibtable[n]


print(fib(8))


def LCW(u, v):
    for r in range(len(u)+1):
        LCW[r][len(v)+1] = 0
    for c in range(len(v)+1):
        LCW[len(u)+1][c] = 0
    maxLCW = 0
    for c in range(len(v)+1, -1, -1):
        for r in range(len(u)+1, -1, -1):
            if u[r] == v[c]:
                LCW[r][c] = 1 + LCW[r+1][c+1]
            else:
                LCW[r][c] = 0
            if LCW[r][c] > maxLCW:
                maxLCW = LCW[r][c]

    return (maxLCW)


print(LCW("secret", "bisect"))

