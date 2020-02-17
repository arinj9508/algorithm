T = int(input())
for tc in range(1, T+1):
    R, C, N = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    grid = [[0]*C for _ in range(R)]

    for i in range(N):
        for j in range(arr[i][0]-1, arr[i][2]):
            for k in range(arr[i][1]-1, arr[i][3]):
                grid[j][k] += 1

    max_grid = 0
    for x in range(R):
        for y in range(C):
            if max_grid < grid[x][y]:
                max_grid = grid[x][y]
    cnt = 0
    for q in range(R):
        for w in range(C):
            if grid[q][w] == max_grid:
                cnt += 1

    print('#{} {}'.format(tc, cnt))
    