def dfs(i, j):
    if maze[i][j] == '3': # 도착지를 찾은 경우
        return 1
    else:
        maze[i][j] = '1' # i, j에 방문을 표시한다
        for k in range(4):  # 4방향
            ni = i + di[k]
            nj = j + dj[k]
            if maze[ni][nj] != '1':  # 통로 또는 도착점
                if dfs(ni, nj) == 1:
                    return 1
        return 0

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]


T = 10
for tc in range(1, T+1):
    # 1 : 벽, 0 : 길, 2 : 출발점, 3 : 도착점
    N = int(input())
    maze = [list(input()) for _ in range(16)]

    si, sj = 0, 0
    for i in range(16):
        for j in range(16):
            if maze[i][j] == '2':
                si, sj = i, j
        if si != 0:  # si > 0 and sj > 0 벽으로 둘러싸여 있으면!!
        # 찾으면 바로 빠져나오기 위해 쓴것!
            break

    print(dfs(si, sj))