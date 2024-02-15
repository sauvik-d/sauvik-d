def expanding(l):
    if len(l) <= 1:
        return True

    prev_diff = abs(l[1] - l[0])
    for i in range(1, len(l)-1):
        diff = abs(l[i+1] - l[i])
        if diff <= prev_diff:
            return False
        prev_diff = diff
    return True


list1 = [1, 3, 7, 2, 9]
list2 = [1, 3, 7, 2, -3]
print("Result is:", expanding(list1))
print("Result is:", expanding(list2))


def sumsquare(seq):
    l = []
    odd = 0
    even = 0
    for i in seq:
        if i % 2 == 0:
            even = even + (i**2)
        else:
            odd = odd + (i**2)
    l.append(odd)
    l.append(even)
    return l


seq1 = [1, 3, 5]
print("SumSquare is", sumsquare(seq1))


def transpose(m):
    num_rows = len(m)
    num_cols = len(m[0])

    transposed = [[0 for _ in range(num_rows)] for _ in range(num_cols)]

    for i in range(num_rows):
        for j in range(num_cols):
            transposed[j][i] = m[i][j]

    return transposed
