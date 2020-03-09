T = int(input())
for tc in range(1,T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    result = []
    cnt = 0
    for i in range(len(arr)-M+1):
        for j in range(M):
            cnt += arr[i+j]
        result.append(cnt)
        cnt = 0

    minn = min(result)
    maxx = max(result)

    final = maxx - minn

    print("#{} {}".format(tc, final))