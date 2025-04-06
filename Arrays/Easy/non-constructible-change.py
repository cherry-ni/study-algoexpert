# Greedy Algorithm
# If we can make all the numbers from 1 to K, and the next number N is less than or equal to K
# then we can extend the range of numbers we can make up to N + K.
# This is because there are no gaps in the sequence from 1 to K and N to K
# and adding N to that range allows us to cover all numbers from 1 to N + K.

# O(nlog(n)) times | O(1) space

def nonConstructibleChange(coins):
    # Write your code here.
    coins.sort()        # O(nlog(n))
    target = 1

    for num in coins :  # O(n)
        if num > target :
            return target + 1

        else :
            target += num
