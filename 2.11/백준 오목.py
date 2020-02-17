def f(i, j):
    c = bd[i][j]
    v = [0]*8
    for k in range(8):
        ni, nj = i+di[k], j+dj[k]
        cnt = 0
        while bd[ni][nj]==c:
            ni, nj = ni + di[k], nj + dj[k]
            cnt += 1
        v[k] = cnt
    for i in range(4):
        if v[i]+v[i+4] == 4:
            return 1
    return 0
# 이중 포문에서 안쪽것을 깰때 flag=1로 셋팅해놓으면
di = [0,1,1,1,0,-1,-1,-1]
dj = [1,1,0,-1,-1,-1,0,1]
bd = [[0]*21 for _ in range(21)]
N = int(input())
ans = -1
stone = [list(map(int, input().split())) for _ in range(N)]
for tc in range(N):
    i, j = stone[tc]
    bd[i][j] = tc%2+1
    if f(i, j) == 1:
        ans = tc+1
        break

print(ans)