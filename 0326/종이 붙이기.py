def f(N):
    if N<2:
        return 1

    else:
        return f(N-1)+2*f(N-2)


T = int(input())
for tc in range(1, T+1):
    N = int(input())//10

    print('#{} {}'.format(tc, f(N)))