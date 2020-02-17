N, M = map(int, input().split())
A = [list(map(int, input().split()))for _ in range(N)]

total = 0
for i in range(N):
    for j in range(M):
        if i == 0:
            total += A[i][j]
        elif i == N-1:
            total += A[i][j]

    if i != 0 and i != N-1:
        total += (A[i][0] + A[i][M-1])
print(total)
