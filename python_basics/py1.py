def solve_rec_rel(n, c):
    t = [0, 0, 0]
    for i in range(3, n+1):
        t.append(t[i-3] + c * i ** 2)

    return t[n]


n_new = 10
c_new = 1
result = solve_rec_rel(n_new, c_new)
print(f"t({n_new}) = {result}")
