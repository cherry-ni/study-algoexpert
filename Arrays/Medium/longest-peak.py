# O(n^2) time | O(1) space
def longestPeak(array):
    result = 0

    for i in range(len(array) - 1) :
        count = 1
        peak = False
        for j in range(i, len(array) - 1) :
            if peak == False and array[j] < array[j + 1] :
                count += 1

            elif peak == False and array[j] > array[j + 1] and count > 1 :
                count += 1
                peak = True

            elif peak == True and array[j] > array[j + 1] :
                count += 1

            else :
                break

        if peak == False: count = 0
        result = max(result, count)

    return result

# O(n) time | O(1) space
def longestPeak2(array):
    result = 0
    count = 0
    peak = False

    idx = 0

    while idx < len(array) - 1 :
        if peak == False and array[idx] < array[idx + 1]:
            count += 1

        elif peak == False and array[idx] > array[idx + 1] and count > 0:
            count += 1
            peak = True

        elif peak == True and array[idx] > array[idx + 1]:
            count += 1

        else:
            if peak :
                result = max(result, count + 1)
                peak = False
                idx -= 1
            count = 0

        idx += 1

    if peak : result = max(result, count + 1)

    return result

def longestPeak3(array) :
    result = 0

    for i in range(1, len(array) - 1) :
        if array[i - 1] < array[i] > array[i + 1] :
            left = i - 1
            right = i + 1

            while left > 0 and array[left - 1] < array[left] :
                left -= 1

            while right < len(array) - 1 and array[right + 1] < array[right] :
                right += 1

            result = max(result, right - left + 1)

    return result

if __name__ == '__main__':
    print(longestPeak([5, 4, 3, 2, 1, 2, 10, 12]))
    print(longestPeak2([5, 4, 3, 2, 1, 2, 10, 12]))
    print(longestPeak([1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3]))
    print(longestPeak2([1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3]))
    print(longestPeak3([1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3]))
    print(longestPeak2([1, 3, 2]))
    print(longestPeak3([1, 3, 2]))
