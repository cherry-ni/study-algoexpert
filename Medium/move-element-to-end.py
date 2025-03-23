# O(n) time | O(1) space
def moveElementToEnd(array, toMove):
    # Write your code here.
    idx = 0
    cnt = 0

    for i in range(len(array)) :
        if array[i] == toMove :
            cnt += 1

        else :
            array[idx] = array[i]
            idx += 1

    for j in range(idx, len(array)) :
        array[j] = toMove

    return array

# O(n) time | O(1) space
def moveElementToEnd2(array, toMove):
    left = 0
    right = len(array) - 1

    while left < right :
        if array[right] == toMove :
            right -= 1
            continue

        if array[left] == toMove :
            array[left], array[right] = array[right], array[left]

        left += 1

    return array

if __name__ == '__main__' :
    print(moveElementToEnd([2, 4, 2, 5, 6, 2, 2], 2))
    print(moveElementToEnd2([2, 1, 2, 2, 2, 3, 4, 2], 2))