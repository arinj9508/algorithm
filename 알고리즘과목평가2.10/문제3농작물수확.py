T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    A1 = 0
    A2 = 0
    B1 = 0
    B2 = 0
    C = 0
    for i in range(N):
        for j in range((N//2)+1, N):
            C += arr[i][j]

    for k in range(N//2):
        for l in range((N//2)+1):
            A1 += arr[k][l]

    for m in range(N//2 + 1):
        for n in range((N//2)+1):
            A2 += arr[m][n]

    for o in range((N//2),N):
        for p in range((N//2)+1):
            B1 += arr[o][p]

    for q in range((N//2)+1, N):
        for r in range((N//2)+1):
            B2 += arr[q][r]

    max1 = max(A1, B1, C)
    min1 = min(A1, B1, C)

    max2 = max(A2, B2, C)
    min2 = min(A2, B2, C)

    result1 = max1 - min1
    result2 = max2 - min2

    final = min(result1, result2)

    print('#{} {}'.format(tc, final))