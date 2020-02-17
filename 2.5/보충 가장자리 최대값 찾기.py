N, M, n, m = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

for i in range(N-n+1):
    for j in range(M-m+1):
        B = [[]*m for _ in range(n)]
        for k in range(n):
            for l in range(m):
                B[k][l].append(A[i+k][j+l])
        C = max(B)
    maxx = 0
    if C > maxx:
        maxx = C
print(maxx)
