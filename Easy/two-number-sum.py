# Solution 1
# O(n^2) time | O(1) space
def twoNumberSum(array, targetSum):
    # Write your code here.
    for i in range(len(array)) :
        for j in range(i + 1, len(array)) :
            if array[i] + array[j] == targetSum :
                return [array[i], array[j]]

    return []

# Solution 2
# O(nlog(n)) time | O(1) space
def twoNumberSum2(array, targetSum):
    array.sort()

    left = 0
    right = len(array) - 1

    while left < right:
        if array[left] + array[right] == targetSum:
            return [array[left], array[right]]

        elif array[left] + array[right] > targetSum:
            right = right - 1

        else:
            left = left + 1

    return []