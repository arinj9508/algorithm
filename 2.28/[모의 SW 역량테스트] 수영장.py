T = int(input())
for tc in range(1,T+1):
    cost = list(map(int, input().split()))  # 1일, 1달, 3달, 1년
    twelve = list(map(int, input().split()))  # 12개월 이용 계획

    plan = []
    for i in range(len(twelve)):
        if twelve[i] != 0:
            plan.append(twelve[i])

    total = []
    # 1일 이용권만 사용
    total.append((cost[0]*sum(plan)))
    # 1달 이용권만 사용
    total.append((cost[1]*len(plan)))
    # 1년 이용권만 사용
    total.append(cost[3])



    print('#{} {}'.format(tc, min(total)))