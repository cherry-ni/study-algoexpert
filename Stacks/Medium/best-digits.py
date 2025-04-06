# O(n) time | O(n) space
def bestDigits(number, numDigits):
    # Write your code here.
    stack = []
    cnt = 0
    for n in number:
        while len(stack) > 0 and int(stack[-1]) < int(n) and cnt < numDigits:
            stack.pop()
            cnt += 1

        stack.append(n)

    while cnt < numDigits:
        stack.pop()
        cnt += 1

    return "".join(stack)

if __name__ == '__main__':
    print(bestDigits("22", 1))