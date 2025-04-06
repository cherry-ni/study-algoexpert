# O(n) time | O(n) space

from collections import deque

def sortedSquaredArray(array):
    # Write your code here.
    result = deque()
    left = 0
    right = len(array) - 1

    while (left <= right):
        left_pow = array[left] ** 2
        right_pow = array[right] ** 2

        if (left_pow >= right_pow):
            result.appendleft(left_pow)
            left += 1

        else:
            result.appendleft(right_pow)
            right -= 1

    return list(result)