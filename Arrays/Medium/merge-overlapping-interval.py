# O(nlog(n)) time | O(n) space
def mergeOverlappingIntervals(intervals):
    # Write your code here.
    result = []
    intervals.sort(key=lambda x: x[0])  # O(nlog(n))

    i = 0
    while i < len(intervals) :
        x = intervals[i][0]
        y = intervals[i][1]
        while i < len(intervals) - 1 and intervals[i + 1][0] <= y :
            y = max(y, intervals[i + 1][1])
            i += 1

        result.append([x, y])
        i += 1

    return result


if __name__ == '__main__':
    array = [
        [1, 2],
        [3, 5],
        [4, 7],
        [6, 8],
        [9, 10]
    ]
    array2 = [      # [1, 10], [2, 3], [4, 5], [6, 7], [8, 9]
        [2, 3],
        [4, 5],
        [6, 7],
        [8, 9],
        [1, 10]
    ]
    print(mergeOverlappingIntervals(array))
    print(mergeOverlappingIntervals(array2))