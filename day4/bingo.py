
n_boards = 0
with open("input.txt", "r") as file:
    file.readline()
    for line in file:
        n_boards += 1
n_boards = n_boards // 6

sequence = list()
boards = dict()

def score(board, marked, draw):
    s = 0
    for n_row in range(5):
        for n_col in range(5):
            if marked[n_row][n_col] == 0:
                s += board[n_row][n_col]
    return s * draw

with open("input.txt", "r") as file:
    sequence = [int(c) for c in file.readline().strip().split(",")]
    for i in range(n_boards):
        file.readline()
        boards[i] = [list(), list()]
        for l in range(5):
            line = file.readline().strip().split()
            boards[i][0].append([int(c) for c in line])
            boards[i][1].append([0] * len(line))

for i, draw in enumerate(sequence):
    for n in boards.keys():
        for n_line, line in enumerate(boards[n][0]):
            if draw in line:
                boards[n][1][n_line][line.index(draw)] = 1
    
    for n in boards.keys():
        sum_col = list()
        for j in range(5):
            sum_col.append(0)

        for n_row in range(5):
            for j, c in enumerate(boards[n][1][n_row]):
                sum_col[j] += c
                if sum_col[j] == 5:
                    print(f"board {n} wins with score {score(boards[n][0], boards[n][1], draw)} here")
                    print(draw)
                    exit()

            if sum(boards[n][1][n_row]) == 5:
                print(f"board {n} wins with score {score(boards[n][0], boards[n][1], draw)}")
                print(draw)
                exit()




