T = int(input())
for tc in range(1, T+1):
    K, N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    a = 0
    result = []
    final = 1
    while True:
        cnt = []
        for i in range(a + 1, a + K + 1):
            if i in arr:
               cnt.append(i)

        if len(cnt) == 0:
            final = 0
            break
        else:
            result.append(max(cnt))
            a = max(cnt)
            del cnt[:]

        if a >= N-K:
            break

    if final != 0:
        final = len(result)

    print("#{} {}".format(tc,final))





