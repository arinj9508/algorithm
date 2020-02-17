T = int(input())
for tc in range(1,T+1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    result1 = []
    for i in range(N):
        cnt1 = 0
        for j in range(N):
            if arr[i][j] == 1:
                cnt1 += 1
            else:
                if cnt1 == K:
                    result1.append(cnt1)
                cnt1 = 0
        if cnt1 != 0 and cnt1 == K:
            result1.append(cnt1)

    result2 = []
    for k in range(N):
        cnt2 = 0
        for l in range(N):
            if arr[l][k] == 1:
                cnt2 += 1
            else:
                if cnt2 == K:
                    result2.append(cnt2)
                cnt2 = 0
        if cnt2 != 0 and cnt2 == K:
            result2.append(cnt2)

    Final = len(result1) + len(result2)

    print('#{} {}'.format(tc, Final))