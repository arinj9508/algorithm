T = 10
for tc in range(1, T+1):
    L = int(input())
    arr = [list(map(int, input().split())) for _ in range(L)]

    cnt_len = []
    for i in range(L):
        s = []
        for j in range(L):
            if arr[j][i] != 0:
                s.append(arr[j][i])

        len_s = len(s)
        cnt = 0
        for k in range(len(s)-1):
            if s[k] == 1 and s[k+1] == 2:
                cnt += 1
        cnt_len.append(cnt)

    result = 0
    for i in cnt_len:
        result += i

    print('#{} {}'.format(tc, result))