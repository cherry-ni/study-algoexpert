# O(n*2^n) time | O(n*2^n) space
def powerset(array):
    # Write your code here.
    result = []
    for cnt in range(len(array) + 1):
        recur(array, result, [], 0, cnt)
    return result


def recur(array, result, path, idx, cnt):
    if len(path) == cnt:
        result.append(path[:])
        return

    for i in range(idx, len(array)):
        path.append(array[i])
        recur(array, result, path, i + 1, cnt)
        path.pop()