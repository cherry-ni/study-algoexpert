# O(n * n!) time | O(n * n!) space
def getPermutations(array):
    # Write your code here.
    if len(array) == 0:
        return []

    result = []
    recur(array, result, [], [False] * len(array))
    return result


def recur(array, result, path, used):
    if len(array) == len(path):
        result.append(path[:])
        return

    for i in range(len(array)):
        if not used[i]:
            used[i] = True
            path.append(array[i])
            recur(array, result, path, used)
            path.pop()
            used[i] = False
