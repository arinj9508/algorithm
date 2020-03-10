T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visit = [0]*401

    for i in range(N):
        first = min(arr[i][0],arr[i][1])
        end = max(arr[i][0],arr[i][1])
        if first%2 == 0:
            first -= 1
        if end%2 == 1:
            end += 1
        for j in range(first, end):
            visit[j] += 1

    print("#{} {}".format(tc, max(visit)))