T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    sum1 = []
    sum2 = []
    sum3 = []
    sum4 = []
    sum5 = []
    sum6 = []

    for i1 in range(0, N-1):
        for j1 in range(0, M-2):
            s1 = 0
            for r in range(0, i1+1):
                for c in range(0, j1+1):
                    s1 += arr[r][c]
            sum1.append(s1)

            for j2 in range(j1 + 1, M-1):
                s2 = 0
                for r in range(0, i1+1):
                    for c in range(j1+1, j2+1):
                        s2 += arr[r][c]
                sum2.append(s2)

                s3 = 0
                for r in range(0, i1+1):
                    for c in range(j2+1, M):
                        s3 += arr[r][c]
                sum3.append(s3)

                s5 = 0
                for r in range(i1+1, N):
                    for c in range(j1+1, j2+1):
                        s5 += arr[r][c]
                sum5.append(s5)

                s6 = 0
                for r in range(i1+1, N):
                    for c in range(j2+1, M):
                        s6 += arr[r][c]
                sum6.append(s6)

            s4 = 0
            for r in range(i1+1, N):
                for c in range(0, j1+1):
                    s4 += arr[r][c]
            sum4.append(s4)

    sum_lst = []
    for i in range(len(sum1)):
        sum_lst.append([sum1[i],sum2[i],sum3[i],sum4[i],sum5[i],sum6[i]])

    result = []
    for i in range(len(sum_lst)):
        result.append(max(sum_lst[i])-min(sum_lst[i]))

    Final = min(result)

    print('#{} {}'.format(tc, Final))