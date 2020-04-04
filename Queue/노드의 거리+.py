T = int(input())
for tc in range(1, T+1):
    # 인접행렬 생성
    V, E = map(int, input().split())  # 노드수, 간선수
    edge = [list(map(int, input().split())) for _ in range(E)] # 연결된 간선
    S, G = map(int, input().split())  # 출발노드, 도착노드

    adj = [[0]*(V+1) for _ in range(V+1)]  # 인접행렬 리스트

    for i in range(E):
        n1 = edge[i][0]
        n2 = edge[i][1]
        adj[n1][n2] = 1
        adj[n2][n1] = 1         # 인접행렬 완성

    Queue = []  # 큐생성
    visited = [0] * (V + 1)
    result = 0
    Queue.append(S)  # 시작점 저장
    visited[S] = 1
    flag = 0

    while Queue:  # 큐가 비어있지 않으면
        n = Queue.pop(0)
        for i in range(1, V + 1):
            if adj[n][i] == 1 and visited[i] == 0:  # i가 인접이고, 방문하지 않았으면
                Queue.append(i)
                visited[i] = visited[n] + 1
                if i == G:
                    result = visited[i] - 1
                    flag = 1
        if flag:
            break
    print('#{} {}'.format(tc, result))