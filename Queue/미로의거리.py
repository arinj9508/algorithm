def f(x, y):
    global n, result
    Queue = []
    Queue.append((x, y))
    visited = [[0]*N for _ in range(N)]
    visited[x][y] = 1
    flag = 0

    while Queue:
        n += 1
        for i in range(len(Queue)):
            a, b = Queue.pop(0)
            for j in range(4):
                X, Y = a + dir_list[j][0], b + dir_list[j][1]
                if 0 <= X < N and 0 <= Y < N:
                    if arr[X][Y] == 0 and visited[X][Y] == 0:
                        Queue.append((X, Y))
                        visited[X][Y] += 1
                    if arr[X][Y] == 3:
                        result = n
                        flag = 1
        if flag:
            break


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int,input())) for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                x, y = i, j

    dir_list = ((-1, 0), (1, 0), (0, -1), (0, 1))
    n = -1
    result = 0
    f(x, y)

    print('#{} {}'.format(tc, result))