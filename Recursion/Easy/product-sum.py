# O(n) time | O(d) space
# Tip: You can use the type(element) function to check whether an item
# is a list or an integer.
def productSum(array):
    # Write your code here.
    result = recur(array, 1)
    return result


def recur(array, depth):
    sum = 0
    for a in array:
        if type(a) is list:
            sum += depth * recur(a, depth + 1)

        else:
            sum += a * depth

    return sum