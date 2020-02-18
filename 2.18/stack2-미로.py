def f(x, y):
    stack = [(x, y)]
    while stack:
        x, y = stack.pop()

        if arr[x][y] == 3:
            return 1
        arr[x][y] = 1

        for k in range(4):
            go_x = x + dir_list[k][0]
            go_y = y + dir_list[k][1]
            if arr[go_x][go_y] != 1:
                stack.append((go_x, go_y))
    return 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [[1]*(N+2)] + [([1] + list(map(int, input())) + [1]) for _ in range(N)] +[[1]*(N+2)]
    # 1은 벽, 2는 출발, 3은 도착
    for i in range(N+2):
        for j in range(N+2):
            if arr[i][j] == 2:
                x, y = i, j

    dir_list = ((-1, 0), (1, 0), (0, -1), (0, 1))
    print('#{} {}'.format(tc, f(x, y)))
