T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]


    rotate = []
    b = [[0] * N for i in range(N)]
    for k in range(3):
        for i in range(N):
            for j in range(N):
                 b[i][j] = arr[N - 1 - j][i]
        rotate.append(b)
        arr = b
        b = [[0]*N for i in range(N)]

    print('#{}'.format(tc))


    for i in range(N):
        for j in range(3):
            print(''.join(map(str,rotate[j][i])),end=' ')
        print()