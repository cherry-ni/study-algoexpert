# O(10^(t-s)) time | O(t-s) space
# def blackjackProbability(target, startingHand):
#     # Write your code here.
#     probability = 0
#     for i in range(1, 11):
#         if target - 4 <= startingHand + i <= target:
#             continue
#
#         elif startingHand + i > target:
#             probability += 0.1
#
#         else:
#             probability += 0.1 * blackjackProbability(target, startingHand + i)
#
#     return round(probability, 3)

# O(10 * (t-s)) time | O(t-s) space
# def blackjackProbability(target, startingHand, memo = None):
#     # Write your code here.
#     if memo is None:
#         memo = {}
#
#     if startingHand in memo:
#         return memo[startingHand]
#
#     d = target - startingHand
#     probability = 0
#
#     # bust
#     probability += 0.1 * (10 - d)
#
#     for i in range(1, d - 4):
#         probability += 0.1 * blackjackProbability(target, startingHand + i)
#
#     memo[startingHand] = round(probability, 3)
#     return memo[startingHand]

def blackjackProbability(target, startingHand):
    # Write your code here.
    if startingHand > target:
        return 1

    if startingHand >= target - 4:
        return 0

    dp = [0.0 for _ in range(target + 11)]

    for hand in range(target + 1, target + 11):
        dp[hand] = 1.0

    for hand in range(target - 1, startingHand - 1, -1):
        probability = 0

        for i in range(1, 11):
            if target - 4 <= hand + i <= target:
                continue

            probability += 0.1 * dp[hand + i]

        dp[hand] = round(probability, 3)

    return dp[startingHand]

if __name__ == '__main__':
    print(blackjackProbability(21, 15))