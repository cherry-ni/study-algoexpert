# O(n^2) time | O(n) space
def threeNumberSum(array, targetSum):
    # Write your code here.
    result = []
    array.sort()

    for idx, num in enumerate(array) :
        second_target_sum = targetSum - num
        left = idx + 1
        right = len(array) - 1

        while left < right :
            if array[left] + array[right] == second_target_sum :
                result.append([num, array[left], array[right]])
                left += 1
                right -= 1

            elif array[left] + array[right] < second_target_sum :
                left += 1

            else :
                right -= 1

    return result

if __name__=='__main__':
    print(threeNumberSum([12, 3, 1, 2, -6, 5, -8, 6], 0))