# O(r*c) time | O(r*c) space

def transposeMatrix(matrix):
    # Write your code here.
    result = []

    row = len(matrix)
    column = len(matrix[0])

    for c in range(column) :
        row_arr = []
        for r in range(row) :
            row_arr.append(matrix[r][c])

        result.append(row_arr)

    return result

matrix = [
    [1, 2, 3],
    [4, 5, 6]
  ]

result = transposeMatrix(matrix)
print(result)