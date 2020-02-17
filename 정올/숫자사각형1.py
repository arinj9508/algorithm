N, M = map(int, input().split())
arr = [[0]*M for _ in range(N)]

for i in range(N):
    for j in range(M):
        arr[i][j] = (5*i) + (j+1)

for i in arr:
    print("".join(map(str, i)))