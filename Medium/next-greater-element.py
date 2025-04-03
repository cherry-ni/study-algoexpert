# O(n) time | O(n) space
def nextGreaterElement(array):
    # Write your code here.
    output = [-1 for _ in range(len(array))]
    stack = []

    for i in range(2 * len(array) - 1):
        ni = i % len(array)
        while stack and stack[-1][1] < array[ni]:
            idx, v = stack.pop()
            output[idx] = array[ni]

        if i < len(array) : stack.append([i, array[i]])

    return output

if __name__ == '__main__':
    print(nextGreaterElement([0, 1, 2, 3, 4]))