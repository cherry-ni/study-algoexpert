# O(4^n * n) time | O(4^n * n) space
mnemonic = [
    ['0'],
    ['1'],
    ['a', 'b', 'c'],
    ['d', 'e', 'f'],
    ['g', 'h', 'i'],
    ['j', 'k', 'l'],
    ['m', 'n', 'o'],
    ['p', 'q', 'r', 's'],
    ['t', 'u', 'v'],
    ['w', 'x', 'y', 'z'],
]

def phoneNumberMnemonics(phoneNumber):
    # Write your code here.
    result = []
    recur(phoneNumber, result, [], 0)
    return result


def recur(array, result, path, idx):
    if len(path) == len(array):
        result.append(''.join(path))    # O(n) time
        return

    for i in range(len(mnemonic[int(array[idx])])):
        path.append(mnemonic[int(array[idx])][i])
        recur(array, result, path, idx + 1)
        path.pop()

if __name__ == '__main__':
    print(phoneNumberMnemonics("1905"))