def rotate(matrix):
    n = len(matrix)
    for offset in range(n >> 1):
        for ix in range(offset, n - offset - 1):
            top = (offset, ix)
            right = (offset + (ix - offset), n - offset - 1)
            bottom = (n - offset - 1, n - offset - (ix - offset) - 1)
            left = (n - offset - (ix - offset) - 1, offset)

            temp = matrix[top[0]][top[1]]
            matrix[top[0]][top[1]] = matrix[left[0]][left[1]]
            matrix[left[0]][left[1]] = matrix[bottom[0]][bottom[1]]
            matrix[bottom[0]][bottom[1]] = matrix[right[0]][right[1]]
            matrix[right[0]][right[1]] = temp
