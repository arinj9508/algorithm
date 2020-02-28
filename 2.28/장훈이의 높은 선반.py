def f(n,k):
    if n == k:
        for i in range(k):
            if L[i] == 1:
                s.append(N_H[i])
        lst.append(sum(s))
        del s[:]
    else:
        L[n] = 0
        f(n+1, k)
        L[n] = 1
        f(n+1, k)

T = int(input())
for tc in range(1, T+1):
    N, B = map(int, input().split())
    N_H = list(map(int, input().split()))

    L = [0]*N
    s = []
    lst = []
    f(0,N)

    minn = []
    for i in lst:
        if i >= B:
            minn.append(i - B)
    # print(minn)
    if len(minn) == 0:
        result = 0
    else:
        result = min(minn)

    print('#{} {}'.format(tc, min(minn)))