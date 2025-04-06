# without sorting
# without using more than constant space

# O(n^2) time | O(1) space
def majorityElement(array):
    # Write your code here.

    for num in array :
        cnt = 0
        for i in range(len(array)) :
            if array[i] == num :
                cnt += 1

        if cnt >= (len(array) // 2 + 1) :
            return num

# O(nlog(n)) time | O(1) space
def majorityElement2(array):
    # Write your code here.
    array.sort()

    return array[len(array) // 2]

# Greedy Algorithm
# O(n) time | O(1) space
def majorityElement3(array):
    majority = array[0]
    cnt = 1

    for i in range(1, len(array)):
        if cnt == 0 :
            majority = array[i]

        cnt += (1 if majority == array[i] else -1)

    return majority

if __name__ == '__main__' :
    print(majorityElement([1, 2, 3, 2, 2, 1, 2]))
    print(majorityElement2([1, 2, 3, 2, 2, 1, 2]))
    print(majorityElement3([1, 2, 3, 2, 2, 1, 2]))