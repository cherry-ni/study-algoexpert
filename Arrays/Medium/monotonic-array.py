# O(n) time | O(1) space

def isMonotonic(array):
    # Write your code here.
    if len(array) <= 1 :
        return True

    pointer = 0
    check = 0

    while pointer < len(array) - 1 :
        if array[pointer] != array[pointer + 1] :
            if check * (array[pointer] - array[pointer + 1]) < 0 :
                return False

            else :
                check = array[pointer] - array[pointer + 1]

        pointer += 1

    return True

def isMonotonic2(array) :
    upward = True
    downward = True

    for i in range(len(array) - 1) :
        if array[i] > array[i + 1] :
            upward = False

        if array[i] < array[i + 1] :
            downward = False

    return upward or downward

if __name__ == '__main__':
    print(isMonotonic([-1, -5, -10, -1100, -1100, -1101, -1102, -9001]))
    print(isMonotonic2([-1, -5, -10, -1100, -1100, -1101, -1102, -9001]))