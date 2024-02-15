def explore((sx, sy), (tx, ty)):
    marked = [[0 for i in range(n)] for j in range(m)]
    marked[sx][sy] = 1
    