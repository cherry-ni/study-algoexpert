# O(n) time | O(n) space
def zeroSumSubarray(nums):
    # Write your code here.
    prefix_sum = [x for x in nums]

    # O(n) time
    for i in range(1, len(nums)):
        prefix_sum[i] = prefix_sum[i - 1] + nums[i]

    print(prefix_sum)

    # O(n) time
    if 0 in prefix_sum : return True

    cnt = {}
    # O(n) time
    for i in range(len(nums)) :
        if prefix_sum[i] in cnt :
            return True

        else :
            cnt[prefix_sum[i]] = 1

    return False

def zeroSumSubarray2(nums):
    prefix_sum = [0]

    current_sum = 0
    for num in nums :
        current_sum += num

        if current_sum in prefix_sum :
            return True

        prefix_sum.append(current_sum)

    return False

if __name__ == '__main__':
    print(zeroSumSubarray([2, 3, 4, -5, -3, 5, 5]))  # [-5, -3, -2, 2, 5]