n, m = map(int, input().split())
arr = [[0]*n for _ in range(n)]

if m == 1:
    for i in range(n):
        for j in range(n):
            arr[i][j] = i+1

if m == 2:
    for k in range(n):
        for l in range(n):
            if k % 2 == 0:
                arr[k][l] = l+1
            else:
                arr[k][l] = n-l

if m == 3:
    for o in range(n):
        for p in range(n):
            arr[o][p] = (o+1)*(p+1)

for final in arr:
    print("".join(map(str, final)))