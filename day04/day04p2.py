import sys


def parse_board():
    with open("input.txt", "r") as f:
        selection = f.readline()
        boards = f.read()

    selection = selection.split(",")
    selection = list(map(lambda x: int(x) + 1, selection))

    boards = boards.replace("  ", " ")
    temp = []
    for board in boards.split("\n\n"):
        rows = board.split("\n")
        t = []
        for e in rows:
            if e == "":
                continue
            e = e.strip().split(" ")
            e = list(map(lambda x: int(x) + 1, e))
            t.append(e)
        temp.append(t)

    boards = temp
    print(selection)
    print(boards)
    return selection, boards


def is_winner(board):
    for i in range(5):
        # Horizontal
        if sum(board[i]) == 0:
            return True
        # Vertical
        running_sum = (
            board[0][i] + board[1][i] + board[2][i] + board[3][i] + board[4][i]
        )
        if running_sum == 0:
            return True
    return False


winners_found = set()
selection, boards = parse_board()
for num in selection:
    for b, board in enumerate(boards):
        for r, row in enumerate(board):
            for c, value in enumerate(row):
                if value != num:
                    continue
                row[c] = 0
                if not is_winner(board):
                    continue
                winners_found.add(b)
                if len(winners_found) == len(boards):
                    remainder = 0
                    for i in board:
                        for j in i:
                            if j != 0:
                                remainder += j - 1
                    num -= 1
                    print(remainder)
                    print(num)
                    print(num * remainder)
                    sys.exit(1)
