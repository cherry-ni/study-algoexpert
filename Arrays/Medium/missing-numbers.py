# O(n) time | O(n) space
def missingNumbers(nums):
    # Write your code here.
    n = len(nums) + 2

    missing_value = set([i for i in range(1, n + 1)])

    for num in nums :
        missing_value.remove(num)

    return list(missing_value)

# O(n) time | O(1) space
def missingNumbers2(nums):
    n = len(nums) + 2

    expected = n * (n + 1) // 2
    actual = sum(nums)

    S = expected - actual

    pivot = S // 2

    expected_left = sum([i for i in range(1, pivot + 1)])
    actual_left = sum([num for num in nums if num <= pivot])

    left = expected_left - actual_left
    right = S - left

    return [left, right]


if __name__ == '__main__' :
    print(missingNumbers([1, 4, 3]))
    print(missingNumbers2([1, 4, 3]))