# O(k^n) time | O(n) space
def staircaseTraversal(height, maxSteps):
    # Write your code here.
    cnt = staircaseTraversalRecursion(0, height, maxSteps, 0)
    return cnt

def staircaseTraversalRecursion(currentHeight, height, maxSteps, cnt):
    if currentHeight == height:
        return cnt + 1

    for s in range(1, maxSteps + 1):
        if currentHeight + s > height:
            continue

        cnt = staircaseTraversalRecursion(currentHeight + s, height, maxSteps, cnt)

    return cnt

if __name__ == '__main__':
    print(staircaseTraversal(4, 2))