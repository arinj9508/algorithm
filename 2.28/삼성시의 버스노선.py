T = int(input())
for tc in range(1, T+1):
    N = int(input())    # N(버스노선수), 1<=N<=500
    AB = [list(map(int, input().split())) for _ in range(N)]   # 1<=A<=B<=5000
    P = int(input())    # 1<=P<=500 P(정류장갯수)
    C = [int(input()) for _ in range(P)]

    contact_station = []
    for i in range(len(AB)):
        for j in range(AB[i][0],AB[i][1]+1):
            contact_station.append(j)

    result = [0]*P
    for i in contact_station:
        for j in range(len(C)):
            if i == C[j]:
                result[j] += 1

    print('#{} {}'.format(tc, " ".join(map(str, result))))