T = int(input())
for tc in range(1, T+1):
    N = int(input())
    # 1 <= T <= 50, 10 <= N <= 300

    N = N // 10
    f = []
    f.append(1)
    f.append(1)
    f.append(3)

    for i in range(3, N+1):
        f.append(f[i-1] + (2*f[i-2]))

    print('#{} {}'.format(tc, f[-1]))
