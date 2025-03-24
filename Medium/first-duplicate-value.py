# O(n) time | O(n) space
def firstDuplicateValue(array):
    # Write your code here.
    count = [0 for _ in range(len(array) + 1)]

    for i in range(len(array)) :
        if count[array[i]] > 0 :
            return array[i]
        else :
            count[array[i]] += 1

    return -1

# O(n) time | O(1) space
def firstDuplicateValue2(array):
    if len(array) <= 1 :
        return -1

    for i in range(len(array)) :
        cur_value = abs(array[i])

        if array[cur_value - 1] < 0:
            return cur_value

        else:
            array[cur_value - 1] *= -1

    return -1

if __name__ == '__main__' :
    # print(firstDuplicateValue([2, 1, 5, 2, 3, 3, 4]))
    print(firstDuplicateValue2([2, 1, 5, 2, 3, 3, 4]))
    # print(firstDuplicateValue([2, 1, 5, 3, 3, 2, 4]))
    # print(firstDuplicateValue2([2, 1, 5, 3, 3, 2, 4]))
    print(firstDuplicateValue2([8, 20, 4, 12, 14, 9, 19, 17, 14, 20, 22, 9, 6, 15, 1, 15, 10, 9, 17, 7, 22, 17]))