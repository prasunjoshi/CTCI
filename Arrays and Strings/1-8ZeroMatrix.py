def zeroMatrix(matrix):
    m = len(matrix)
    n = len(matrix[0])
    rows = []
    cols = []

    for x in range(m):
        for y in range(n):
            if matrix[x][y] == 0:
                rows.append(x)
                cols.append(y)
    for row in rows:
        for i in range(n):
            matrix[row][i] = 0

    for col in cols:
        for i in range(m):
            matrix[i][col] = 0
    return matrix

print(zeroMatrix([[1,2,3],[4,0,5],[6,7,8]]))

