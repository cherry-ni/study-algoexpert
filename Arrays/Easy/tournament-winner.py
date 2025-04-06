# O(n) time | O(k) space

from collections import defaultdict


def tournamentWinner(competitions, results):
    # Write your code here.
    score = defaultdict(int)

    for round in range(len(competitions)):
        home = competitions[round][0]
        away = competitions[round][1]

        if results[round] == 1:
            score[home] += 3

        else:
            score[away] += 3

    winner = max(score, key=score.get)

    return winner