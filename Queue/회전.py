T = int(input())
for tc in range(1,T+1):
    N, M = map(int, input().split())
    n = list(map(int, input().split()))


    for i in range(M):
        q = [0] * N
        q[-1] += n[0]
        for j in range(1,N):
            q[j-1] += n[j]
        n = q

    print('#{} {}'.format(tc, n[0]))