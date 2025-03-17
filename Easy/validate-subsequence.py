# O(n) time | O(1) space

def isValidSubsequence(array, sequence):
    # Write your code here.
    i = 0;
    j = 0

    while (i < len(array) and j < len(sequence)):
        if (array[i] == sequence[j]):
            i += 1
            j += 1

        else:
            i += 1

    if (j == len(sequence)):
        return True
    else:
        return False