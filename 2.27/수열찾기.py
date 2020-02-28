def dfs(x,y):
    global k
    visited[x][y] = 1
    k += 1
    s.append(arr[x][y])
    if arr[x][y] == N_num[-1] and len(s) == N:
        return 1
    else:
        for i in range(4):
            X, Y = x + dir_list[i][0], y + dir_list[i][1]
            if 0 <= X < M and 0 <= Y < M:
                if arr[X][Y] == N_num[k] and visited[X][Y] == 0:
                    if dfs(X,Y):
                        return 1
        return 0


T = int(input())
for tc in range(1, T+1):
    N_num = list(map(int, input().split()))
    N = N_num.pop(0)
    M = int(input())
    arr = [list(map(int, input().split())) for _ in range(M)]

    dir_list = ((-1, 0), (1, 0), (0, -1), (0, 1))
    result = 0
    for x in range(M):
        for y in range(M):
            if arr[x][y] == N_num[0]:
                s = []
                k = 0
                visited = [[0]*M for _ in range(M)]
                if dfs(x,y):
                    result = 1
                    break
        if result == 1:
            break
    print("#{} {}".format(tc, result))