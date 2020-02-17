def dfs(n, N):
    visited[n] = 1
    s.append(n)
    for i in range(N+1):
        if adj[n][i] == 1 and visited[i] == 0:
            dfs(i, N)


T = int(input())
for tc in range(1, T+1):
    s = []
    N, E = map(int, input().split())
    adj = [[0]*(N+1) for _ in range(N+1)]
    edge = [list(map(int, input().split())) for _ in range(E)]
    visited = [0]*(N+1)
    for i in range(E):
         n1 = edge[i][0]
         n2 = edge[i][1]
         adj[n1][n2] = 1   # 인접행렬 완성

    dfs(0, N)
    s = map(str, s)

    print('#{} {}'.format(tc, " ".join(s)))