# O(n^2) time | O(n) space
def arrayOfProducts(array):
    result = [1 for x in range(len(array))]

    for i in range(len(array)) :
        for j in range(len(array)) :
            if i != j :
                result[i] *= array[j]

    return result

if __name__ == '__main__':
    print(arrayOfProducts([5, 1, 4, 2]))