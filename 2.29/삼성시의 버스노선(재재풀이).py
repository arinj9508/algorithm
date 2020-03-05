T = int(input())
for tc in range(1, T+1):
    N = int(input())
    AB = [list(map(int, input().split())) for _ in range(N)]
    P = int(input())
    C = [int(input()) for _ in range(P)]

    result = [0]*P
    for i in range(N):
        ab = list(range(AB[i][0], AB[i][1] + 1))
        for j in range(P):
            if C[j] in ab:
                result[j] += 1

    print('#{} {}'.format(tc, " ".join(map(str, result))))