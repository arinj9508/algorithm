T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]


    cnt1 = 0
    len_struc1 = [0]
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1:
                cnt1 += 1
            else:
                if cnt1 >= 2:
                    len_struc1.append(cnt1)
                cnt1 = 0
        if cnt1 != 0:
            len_struc1.append(cnt1)

    cnt2 = 0
    len_struc2 = [0]
    for k in range(M):
        for l in range(N):
            if arr[l][k] == 1:
                cnt2 += 1
            else:
                if cnt2 >= 2:
                    len_struc2.append(cnt2)
                cnt2 = 0
        if cnt2 != 0:
            len_struc2.append(cnt2)


    max1 = max(len_struc1)
    max2 = max(len_struc2)

    max3 = max(max1, max2)

    print('#{} {}'.format(tc, max3))