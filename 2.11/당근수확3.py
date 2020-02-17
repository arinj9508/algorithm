T = int(input())
for tc in range(1, T+1):
    # 1<=T<=50, 5<=N, M<=20, 0<=C<=10
    N, M = map(int, input().split())
    area = [list(map(int, input().split())) for _ in range(N)]

    sum1 = []
    sum2 = []
    sum3 = []

    for i in range(N-1):
        for j in range(M-1):
            s1 = 0
            for r in range(i+1):
                for c in range(j+1):
                    s1 += area[r][c]
            sum1.append(s1)

            s2 = 0
            for r in range(i+1):
                for c in range(j+1, M):
                    s2 += area[r][c]
            sum2.append(s2)

            s3 = 0
            for r in range(i+1, N):
                for c in range(M):
                    s3 += area[r][c]
            sum3.append(s3)

    sum_lst = []
    for i in range(len(sum1)):
        sum_lst.append([sum1[i],sum2[i],sum3[i]])

    result = []
    for i in range(len(sum_lst)):
        result.append(max(sum_lst[i])-min(sum_lst[i]))

    final = min(result)

    print('#{} {}'.format(tc, final))