dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    result = []
    for i in range(N):
        for j in range(M):
            sum = 0
            for k in range(1, arr[i][j]+1):
                for l in range(4):
                    nextX = i + dx[l]*k
                    nextY = j + dy[l]*k
                    if 0 <= nextX < N and 0 <= nextY < M:
                        sum += arr[nextX][nextY]
            sum += arr[i][j]
            result.append(sum)

    print('#{} {}'.format(tc, max(result)))