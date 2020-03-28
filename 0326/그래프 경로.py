def dfs(V, start, end):
    visited = [0]*(V+1)
    stack = []
    stack.append(start)
    visited[start] = 1
    while stack:
        n = stack.pop()
        visited[n] = 1

        if n == end:
            return 1

        for t in adj[n]:
            if visited[t] == 0:
                stack.append(t)

    return 0


T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())

    adj = [[] for _ in range(V+1)]
    for _ in range(E):
        n1, n2 = map(int, input().split())
        adj[n1].append(n2)

    start, end = map(int, input().split())



    print('#{} {}'.format(tc, dfs(V, start, end)))