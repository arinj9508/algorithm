T = int(input())
for tc in range(1, T+1):
    sudoku = [list(map(int, input().split())) for _ in range(9)]

    row = []
    for i in range(9):
        for j in range(10):
            row.append(sudoku[i][j])
        print(row)