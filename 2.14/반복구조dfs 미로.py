def f2(i, j): # 반복구조 dfs
    s = []
    used = [[0]*16 for _ in range(16)]
    s.append((i, j))
    used[i][j] = 1
    while len(s)!=0:
        i, j = s.pop()
        if maze[i][j]=='3': # 목적지에 도착
            return 1
        for k in range(4):  # 네방향 탐색
            ni = i + di[k]
            nj = j + dj[k]
            if maze[ni][nj] != '1' and used[ni][nj]==0:
                s.append((ni, nj))
                used[ni][nj] = 1
    return 0

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
T = 10
for tc in range(1, T+1):
    N = int(input())
    maze = [list(input()) for _ in range(16)]
    si, sj = 0, 0
    for i in range(16):
        for j in range(16):
            if maze[i][j]=='2':
                si, sj = i, j
                break
        if si!=0: # si>0 and sj>0
            break

    print(f2(si, sj))