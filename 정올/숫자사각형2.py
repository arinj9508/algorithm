# 정올- 1856: 숫자사각형2

n, m = map(int, input().split())
arr = [[0]*m for _ in range(n)]

for i in range(n):
    for j in range(m):
        if i % 2 == 0:
            arr[i][j] += (5*i)+j+1
        else:
            arr[i][j] += (i+1)*5-j

for final in arr:
    print("".join(map(str, final)))