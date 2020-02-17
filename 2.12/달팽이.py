T = int(input())
for tc in range(1, T+1):
    N= int(input())
    arr = [[0]*N for _ in range(N)]

    x = 0
    y = -1
    di = 1
    k = 1
    len = N
    while True:
        for i in range(len):
            y += di
            arr[x][y] = k
            k += 1
        len -= 1

        if len == 0:
            break

        for j in range(len):
            x += di
            arr[x][y] = k
            k += 1
        di *= -1

    print('#{}'.format(tc))

    for i in arr:
        print(" ".join(map(str, i)))