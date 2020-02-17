N, M, n, m = map(int, input().split())
A = [list(map(int, input().split()))for _ in range(M)]


for i in range(N-n+1):
    for j in range(M-m+1):
        total = 0
        for k in range(n):
            for l in range(m):
                total += A[i+k][j+l]
    maxx = 0
    if maxx < total:
        maxx = total
print(maxx)