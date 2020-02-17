T = int(input())
for tc in range(1, T+1):
    N = int(input())
    area = [list(map(int, input().split())) for _ in range(N)]

    field1 = []
    field2 = []

    for i in range(N):
        for j in range(N):
            if area[i][j] == 1:
                field1.append(i)
                field2.append(j)

    i_min = min(field1)
    j_min = min(field2)
    i_max = max(field1)
    j_max = max(field2)

    pig = 0
    for i in range(i_min+1):
        for j in range(j_min+1):
            if area[i][j] == 2:
                pig += 1

    for i in range(i_min+1):
        for j in range(j_max, N):
            if area[i][j] == 2:
                pig += 1

    for i in range(i_max, N):
        for j in range(j_min+1):
            if area[i][j] == 2:
                pig += 1

    for i in range(i_max, N):
        for j in range(j_max, N):
            if area[i][j] == 2:
                pig += 1


    print('#{} {}'.format(tc, pig))