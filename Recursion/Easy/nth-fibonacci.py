def getNthFib(n):
    # Write your code here.
    if n == 1: return 0
    if n == 2: return 1

    return getNthFib(n - 1) + getNthFib(n - 2)


if __name__ == '__main__':
    print(getNthFib(6))     # 0, 1, 1, 2, 3, 5