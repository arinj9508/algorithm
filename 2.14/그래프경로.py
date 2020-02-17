'''
def dfs(n, V):
    s = [] # 스택생성
    used = [0]*(V+1) # 중복확인
    s.append(n) #시작점 저장
    used[n] = 1
    while len(s) != 0: # 스택에 비어있지 않으면
        n = s.pop()
        for i in range(1, V+1):
            if adj[n][i] == 1 and used[i] == 0: # i가 인접이고, 스택에 들어있지 않으면
                s.append(i) # 인접목록 추가
                used[i] = 1
    if used[V] == 1:
        return 1
    else:
        return 0
'''

def dfs(n, e, V):
    if n == e:  # 찾는 목적지에 도착하면
        return 1



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
        adj[n1][n2] = 1     # 인접행렬 완성

    print('#{} {}'.format(tc, dfs(S, G)))