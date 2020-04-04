T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())            # 3<=N<=20, N<=M<=100, 1<=Ci<=20
    m = list(map(int, input().split()))

    n = []
    for i in range(N):
        n.append((m[i],i+1))

    i = 0
    while len(n) != 1:
        n[0][0] //= 2
        if n[0][0] == 0:
            if N + i < M:
                n.pop(0)
                n.append([m[N + i], N + i + 1])
                i += 1
            elif N + i >= M:
                n.pop(0)
        else:
            n.append(n.pop(0))

    print('#{} {}'.format(tc, n[0][1]))
