T = int(input())
for tc in range(1, T+1):
    N = list(map(str, input()))
    M = list(map(str, input()))

    # 5 <= N <= 100, 10 <= M <= 1000, N <= M
    result = 10
    for i in range(len(M)-len(N)+1):
        cnt = 0
        for j in range(len(N)):
            if M[i+j] == N[j]:
                cnt += 1
        if cnt == len(N):
            result = 1

    if result != 1:
        result = 0

    print('#{} {}'.format(tc, result))
