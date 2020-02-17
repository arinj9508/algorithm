N = int(input())
arr = [[0]*N for _ in range(N)]

for i in range(N):
    for j in range(N):
        arr[i][j] = (4*j) + (i+1)

for k in arr:
    print("".join(map(str, k)))