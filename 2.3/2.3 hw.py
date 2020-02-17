import sys
sys.stdin = open('2.3hw.txt', 'r')

T = 10
for tc in range(1, T+1):
    N = int(input())
    R = 100
    C = 100
    arr2 = [list(map(int, input().split())) for _ in range(R)]
    row_sum = [0]*100
    column_sum = [0]*100
    a_diagonal = 0
    b_diagonal = 0

    for i in range(R):
        for j in range(C):
            row_sum[i] += arr2[i][j]
            column_sum[i] += arr2[j][i]
        a_diagonal += int(arr2[i][i])
        b_diagonal += int(arr2[i][99-i])

        max_row = row_sum[0]
        for x in range(100):
            if row_sum[x] > max_row:
                max_row = row_sum[x]
        max_column = column_sum[0]
        for y in range(100):
            if column_sum[y] > max_column:
                max_column = column_sum[y]

    result = max(max_row, max_column, a_diagonal, b_diagonal)

    print('#{} {}'.format(tc, result))