# O(n) time | O(1) space
def bestSeat(seats):
    # Write your code here.
    longest_empty_start = 0
    longest_empty_end = -1

    i = 0
    while i < len(seats) :
        if seats[i] == 0 :
            start = i
            j = i
            while seats[j] == 0:
                end = j
                j += 1

            if end - start > longest_empty_end - longest_empty_start :
                longest_empty_start = start
                longest_empty_end = end

            i = j

        else :
            i += 1

    return (longest_empty_start + longest_empty_end) // 2

if __name__ == '__main__':
    print(bestSeat([1, 0, 1]))  # 1은 찬 자리, 0은 빈 자리