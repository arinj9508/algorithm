T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(str, input())) for _ in range(N)]

    result = []
    for i in range(N):
        for j in range(N-M+1):
            cnt1 = 0
            for k in range(M//2):
                if arr[i][j+k] == arr[i][j+M-1-k]:
                    cnt1 += 1

            if cnt1 == M//2:
                for x in range(M):
                    result.append(arr[i][x+j])

    for l in range(N):
        for m in range(N-M+1):
            cnt2 = 0
            for n in range(M//2):
                if arr[m+n][l] == arr[m+M-1-n][l]:
                    cnt2 += 1

            if cnt2 == M // 2:
                for y in range(M):
                    result.append(arr[y+m][l])

    print('#{} {}'.format(tc, "".join(map(str, result))))