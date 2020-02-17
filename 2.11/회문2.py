T = 10
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(str, input())) for _ in range(100)]

    result = 0
    for n in range(1, 101):
        for i in range(100):
            for j in range(101 - n):
                cnt1 = 0
                for k in range(n // 2):
                    if arr[i][j+k] == arr[i][j+n-1-k]:
                        cnt1 += 1
                if cnt1 == n//2:
                    if result < n:
                        result = n

    for m in range(1, 101):
        for x in range(100):
            for y in range(101 - m):
                cnt2 = 0
                for z in range(m // 2):
                    if arr[y+z][x] == arr[y+m-1-z][x]:
                        cnt2 += 1
                if cnt2 == m//2:
                    if result < m:
                        result = m

    print('#{} {}'.format(tc, result))