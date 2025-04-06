# O(n) time | O(n) space
def collidingAsteroids(asteroids):
    # Write your code here.
    stack = []
    for i in range(len(asteroids)):
        while stack and stack[-1] > 0 and asteroids[i] < 0:
            if abs(stack[-1]) < abs(asteroids[i]):
                stack.pop()

            elif abs(stack[-1]) == abs(asteroids[i]):
                stack.pop()
                break

            else:
                break

        else:
            stack.append(asteroids[i])

    return stack
