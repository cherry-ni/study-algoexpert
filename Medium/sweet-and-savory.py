# O(n^2) time | O(n) space
def sweetAndSavory(dishes, target):
    # Write your code here.
    # O(n) space
    sweet = []
    savory = []

    # O(n) time
    for taste in dishes :
        if taste < 0 :
            sweet.append(taste)

        else :
            savory.append(taste)

    if len(sweet) <= 0 or len(savory) <= 0 :
        return [0, 0]

    # O(nlog(n))
    sweet.sort()
    savory.sort()

    best_paring = [0, 0]

    # O(n^2)
    for i in range(len(sweet)) :
        for j in range(len(savory)) :
            if sweet[i] + savory[j] > target :
                break

            if best_paring == [0, 0] and target - (sweet[i] + savory[j]) >= 0 :
                best_paring[0] = sweet[i]
                best_paring[1] = savory[j]

            elif best_paring != [0, 0] and target - (best_paring[0] + best_paring[1]) > target - (sweet[i] + savory[j]) >= 0 :
                best_paring[0] = sweet[i]
                best_paring[1] = savory[j]

    return best_paring

# O(nlog(n)) time | O(n) space
def sweetAndSavory2(dishes, target):
    # O(n) space
    sweet = [d for d in dishes if d < 0]
    savory = [d for d in dishes if d > 0]

    if not sweet or not savory :
        return [0, 0]

    # O(nlog(n))
    sweet.sort(reverse = True)
    savory.sort()

    best_pairing = [0, 0]
    closest_diff = float('inf')

    i, j = 0, 0
    while i < len(sweet) and j < len(savory):
        curr_sum = sweet[i] + savory[j]
        cur_diff = target - curr_sum

        if closest_diff > cur_diff >= 0 :
            best_pairing = [sweet[i], savory[j]]
            closest_diff = cur_diff

        if curr_sum < target:
            j += 1
        else:
            i += 1

    return best_pairing

if __name__ == '__main__' :
    print(sweetAndSavory([17, 37, 12, -102, 53, 49, -90, 102, 49, 16, 52], 12))
    print(sweetAndSavory2([2, 5, -4, -7, 12, 100, -25], 5))