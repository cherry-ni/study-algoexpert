# BFS
# O(w * h) time | O(w * h) space
from collections import deque

def revealMinesweeper(board, row, column):
    # Write your code here.
    dc = [1, 1, 0, -1, -1, -1, 0, 1]
    dr = [0, 1, 1, 1, 0, -1, -1, -1]

    queue = deque([(row, column)])

    while queue:
        r, c = queue.popleft()

        if board[r][c] == "M":
            board[r][c] = "X"

        elif board[r][c] == "H":
            cnt = 0
            newQueue = deque()

            for i in range(8):
                nr = r + dr[i]
                nc = c + dc[i]

                if nr < 0 or nr >= len(board) or nc < 0 or nc >= len(board[0]):
                    continue

                if board[nr][nc] == "M":
                    cnt += 1

                newQueue.append((nr, nc))

            board[r][c] = str(cnt)

            if cnt == 0:
                queue += newQueue

        else:
            continue

    return board

if __name__ == '__main__':
    board = [
        ["H", "H", "H", "H", "M"],
        ["H", "1", "M", "H", "1"],
        ["H", "H", "H", "H", "H"],
        ["H", "H", "H", "H", "H"]
    ]
    row = 3
    column = 4
    '''
    [
        ["0", "1", "H", "H", "M"],
        ["0", "1", "M", "2", "1"],
        ["0", "1", "1", "1", "0"],
        ["0", "0", "0", "0", "0"]
    ]
    '''
    newBoard = revealMinesweeper(board, row, column)
    for r in range(len(newBoard)):
        print(newBoard[r])
