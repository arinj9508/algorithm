T = int(input())

for t in range(1, T + 1):
    N = int(input())
    C = [list(map(int, input().split())) for _ in range(N)]  # 구역별 당근

    # 각 구역별 최대와 최소의 차이를 구해라
    carrots = [0] * 4

    for i in range(N):
        for j in range(N):
            if j > i and i < N - 1 - j:
                carrots[0] += C[i][j]
            elif j > i and i > N - 1 - j:
                carrots[1] += C[i][j]
            elif i > j and i > N - 1 - j:
                carrots[2] += C[i][j]
            else:
                carrots[3] += C[i][j]

    print("#{} {}".format(t, max(carrots) - min(carrots)))
