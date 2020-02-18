def f(n,k):
    global minn

    if minn < sum(p):
        return

    if n == k:
        if sum(p) < minn:
            minn = sum(p)
            return
    else:
        for j in range(k):
            if used[j] == 0:
                used[j] = 1
                p.append(arr[n][j])
                f(n+1,k)
                used[j] = 0
                p.pop()

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    minn = 9*N
    used = [0]*N
    p = []
    f(0,N)
    print('#{} {}'.format(tc, minn))


def f(r, k, s): # 행, 배열의 크기 n-1까지 선택한 웝소의합
    global minV
    if r == k: #모든 면에서 선택완료
        if minV > s:
