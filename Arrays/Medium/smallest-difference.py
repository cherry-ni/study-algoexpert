# O(n*m) time | O(1) space
def smallestDifference(arrayOne, arrayTwo):
    # Write your code here.
    arrayOne.sort()             # O(nlog(n))
    arrayTwo.sort()             # O(mlog(m))

    result_arr = [arrayOne[0], arrayTwo[0]]
    smallest_diff = abs(arrayOne[0] - arrayTwo[0])

    for i in range(len(arrayOne)) :         # O(n)
        curr_diff = abs(arrayOne[i] - arrayTwo[0])

        for j in range(len(arrayTwo)) :     # O(m)
            new_diff = abs(arrayOne[i] - arrayTwo[j])

            if new_diff < smallest_diff :
                result_arr = [arrayOne[i], arrayTwo[j]]
                smallest_diff = new_diff

            if curr_diff < new_diff :
                break

    return result_arr

# O(nlog(n) + mlog(m)) time | O(1) space
def smallestDifference2(arrayOne, arrayTwo):
    # Write your code here.
    arrayOne.sort()             # O(nlog(n))
    arrayTwo.sort()             # O(mlog(m))

    result_arr = []
    smallest_diff = float("inf")
    pointer_one = 0
    pointer_two = 0

    while pointer_one < len(arrayOne) and pointer_two < len(arrayTwo):      # O(n + m)
        curr_diff = abs(arrayOne[pointer_one] - arrayTwo[pointer_two])

        if curr_diff < smallest_diff :
            result_arr = [arrayOne[pointer_one], arrayTwo[pointer_two]]
            smallest_diff = curr_diff

        if arrayOne[pointer_one] < arrayTwo[pointer_two]:
            pointer_one += 1

        elif arrayOne[pointer_one] > arrayTwo[pointer_two]:
            pointer_two += 1

        else :
            return [arrayOne[pointer_one], arrayTwo[pointer_two]]

    return result_arr


if __name__ == '__main__' :
    print(smallestDifference([-1, 5, 10, 20, 28, 3], [26, 134, 135, 15, 17]))
    print(smallestDifference2([-1, 5, 10, 20, 28, 3], [26, 134, 135, 15, 17]))