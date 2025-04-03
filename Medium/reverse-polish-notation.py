# O(n) time | O(n) space
def reversePolishNotation(tokens):
    # Write your code here.
    operator = {"+", "-", "*", "/"}
    stack = []

    for i in range(len(tokens)):
        if tokens[i] in operator:
            b = stack.pop()
            a = stack.pop()

            if tokens[i] == "+" : stack.append(str(int(a) + int(b)))
            if tokens[i] == "-" : stack.append(str(int(a) - int(b)))
            if tokens[i] == "*" : stack.append(str(int(a) * int(b)))
            if tokens[i] == "/" : stack.append(str(int(int(a) / int(b))))

        else:
            stack.append(tokens[i])

    return int(stack.pop())

if __name__ == '__main__':
    print(reversePolishNotation(["50", "3", "17", "+", "2", "-", "/"]))