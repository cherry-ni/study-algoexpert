def sortStack(stack):
    # Write your code here.
    sort(stack)

    return stack

def sort(stack):
    if len(stack) == 0:
        return

    top = stack.pop()
    sort(stack)
    insert(top, stack)

def insert(value, stack):
    if len(stack) == 0 or stack[-1] <= value:
        stack.append(value)
        return

    top = stack.pop()
    insert(value, stack)
    stack.append(top)

if __name__ == '__main__':
    print(sortStack([-5, 2, -2, 4, 3, 1]))