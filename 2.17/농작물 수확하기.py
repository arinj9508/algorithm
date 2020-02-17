T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]

    summ = 0
    for i in range((N//2)+1):
        if i == N//2:
            summ += sum(arr[i])

        else:
            summ += sum(arr[i][((N//2)-i):((N//2)+1+i)])
            summ += sum(arr[N-1-i][((N//2)-i):((N//2)+i+1)])

    print('#{} {}'.format(tc, summ))
