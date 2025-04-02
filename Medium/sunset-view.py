# O(n) time | O(n) space
def sunsetViews(buildings, direction):
    # Write your code here.
    answer = []
    height = 0

    if direction == "EAST":
        for i in range(len(buildings) - 1, -1, -1):
            if buildings[i] > height:
                answer.append(i)
                height = buildings[i]

        return answer[::-1]

    else:
        for i in range(len(buildings)):
            if buildings[i] > height:
                answer.append(i)
                height = buildings[i]

        return answer

def sunsetViews2(buildings, direction):
    answer = []

    startIdx = 0 if direction == "EAST" else len(buildings) - 1
    step = 1 if direction == "EAST" else -1

    idx = startIdx
    while idx >= 0 and idx < len(buildings):
        height = buildings[idx]
        while len(answer) > 0 and buildings[answer[-1]] <= height:
            answer.pop()
        answer.append(idx)

        idx += step

    if direction == "WEST":
        return answer[::-1]

    return answer

if __name__ == '__main__' :
    print(sunsetViews([3, 5, 4, 4, 3, 1, 3, 2], "EAST"))
    print(sunsetViews2([3, 5, 4, 4, 3, 1, 3, 2], "EAST"))