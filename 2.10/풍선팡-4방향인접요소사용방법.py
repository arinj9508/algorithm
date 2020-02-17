T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    result = []
    for i in range(N):
        for j in range(M):
            sum = 0
            for k in range(1, arr[i][j]+1):
                for l in range(4):
                    testX = i + dx[l]*k
                    testY = j + dy[l]*k
                    if 0 <= testX < N and 0 <= testY < M:
                        sum += arr[testX][testY]
            sum += arr[i][j]
            result.append(sum)

    max_result = max(result)

    print('#{} {}'.format(tc, max_result))