# O(n*m) time | O(n*m) space

def spiralTraverse(array):
    # Write your code here.
    result = []

    top = -1
    left = -1
    bottom = len(array)
    right = len(array[0])

    r = 0
    c = 0
    while left + 1 < right and top + 1 < bottom :
        for c in range(left + 1, right) :
            result.append(array[r][c])
        top += 1

        for r in range(top + 1, bottom) :
            result.append(array[r][c])
        right -= 1

        if top + 1 < bottom :
            for c in range(right - 1, left, -1) :
                result.append(array[r][c])
            bottom -= 1

        if left + 1 < right :
            for r in range(bottom - 1, top, -1) :
                result.append(array[r][c])
            left += 1

    return result

if __name__ == '__main__' :
    array = [
      [1, 2, 3, 4],
      [12, 13, 14, 5],
      [11, 16, 15, 6],
      [10, 9, 8, 7]
    ]
    print(spiralTraverse(array))

    array2 = [
        [1, 2, 3, 4],
        [10, 11, 12, 5],
        [9, 8, 7, 6]
    ]
    print(spiralTraverse(array2))