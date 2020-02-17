T = int(input())
for tc in range(1, T+1):
    sudoku = [list(map(int, input().split())) for _ in range(9)]

    result = 1
    for i in range(9):
        row = []
        column = []
        for j in range(9):
            row.append(sudoku[i][j])
            column.append(sudoku[j][i])
        if len(set(row)) != 9:
            result = 0
        if len(set(column)) != 9:
            result = 0

    square = [[] for _ in range(9)]
    for i in range(0, 9, 3):
        for j in range(0,3):
            square[i].extend(sudoku[i+j][:3])
            square[i+1].extend(sudoku[i+j][3:6])
            square[i+2].extend(sudoku[i+j][6:])

    for i in range(9):
        if len(set(square[i])) != 9:
            result = 0
            break


    print('#{} {}'.format(tc, result))