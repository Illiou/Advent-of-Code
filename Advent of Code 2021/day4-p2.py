import numpy as np

problem_file_path = "input/d4.txt"

with open(problem_file_path, "r") as problem_file:
    draw_pool = list(map(int, problem_file.readline().split(",")))
    problem_file.readline()
    boards = []
    lines = problem_file.readlines()
    for i in range(0, len(lines), 6):
        boards.append(np.array([line.split() for line in lines[i:i+5]], dtype=int))

is_number_drawn = np.zeros((len(boards), 5, 5), dtype=bool)

winning_board = -1
winning_draw = -1
finished_boards = []
for draw in draw_pool:
    for i, board in enumerate(boards):
        if i in finished_boards:
            continue
        if len(pos := np.argwhere(board == draw)) > 0:
            is_number_drawn[i][tuple(pos[0])] = True
            if np.all(is_number_drawn[i], axis=0).any() or np.all(is_number_drawn[i], axis=1).any():
                winning_board = i
                winning_draw = draw
                finished_boards.append(winning_board)

print(winning_board, winning_draw, boards[winning_board][~is_number_drawn[winning_board]].sum() * winning_draw)

