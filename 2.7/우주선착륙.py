T = int(input())
for tc in range(1, T+1):
    N, M, K, H = map(int, input().split())
    land = [list(map(int, input().split())) for _ in range(N)]


    possible = 0
    for i in range(N - 2):
        for j in range(M - 2):
            space = [[0] * 3 for _ in range(3)]
            for k in range(3):
                for l in range(3):
                    space[k][l] += land[i+k][j+l]

            min_num = space[0][0]
            max_num = space[0][0]
            for q in range(3):
                for w in range(3):
                    if q != 1 or w != 1:
                        if min_num > space[q][w]:
                            min_num = space[q][w]
                        if max_num < space[q][w]:
                            max_num = space[q][w]


            if max_num - min_num <= K and  min_num <= space[1][1] and space[1][1] - min_num <= H:
                possible += 1

    print('#{} {}'.format(tc, possible))