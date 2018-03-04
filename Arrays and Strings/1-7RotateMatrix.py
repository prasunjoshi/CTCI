def rotateMatrix(matrix):
    n = len(matrix)
    for layer in range(n//2):
        first,last = layer,n-layer-1
        for i in range(first, last):
            top = matrix[layer][i]

            matrix[layer][i] = matrix[-i-1][layer]

            matrix[-i-1][layer] = matrix[-layer-1][-i-1]

            matrix[-layer-1][-i-1] = matrix[i][-layer-1]

            matrix[i][-layer-1] = top
    return matrix

print(rotateMatrix([[1,2,3],[4,5,6],[7,8,9]]))


