T = 10
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(str, input())) for _ in range(8)]

    result = 0
    for i in range(8):
        for j in range(9 - N):
            cnt1 = 0
            for k in range(N//2):
                if arr[i][j+k] == arr[i][j+N-1-k]:
                    cnt1 += 1
                else:
                    break
            if cnt1 == N // 2:
                result += 1

    for l in range(8):
        for m in range(9 - N):
            cnt2 = 0
            for n in range(N//2):
                if arr[m+n][l] == arr[m+N-1-n][l]:
                    cnt2 += 1
            if cnt2 == N // 2:
                result += 1

    print('#{} {}'.format(tc, result))