arr = [list(map(int, input().split())) for _ in range(19)]
result = 10
grid = []

cnt1 = 0 # 가로방향 검은돌 탐색

for i in range(19):               #가로 방향의 검은 돌이 5개 있는지 확인
    for j in range(19):
        if arr[i][j] == 1:
            cnt1 += 1
        else:
            if cnt1 == 5:
                result = 1
                grid.append(i)
                grid.append(j - 5)
                break
            else:
                cnt1 = 0

cnt2 = 0 # 가로방향 하얀돌 탐색

for k in range(19):               #가로 방향의 하얀 돌이 5개 있는지 확인
    for l in range(19):
        if arr[k][l] == 2:
            cnt2 += 1
        else:
            if cnt2 == 5:
                result = 2
                grid.append(k)
                grid.append(l - 5)
            cnt2 = 0

cnt3 = 0 # 세로방향 검은돌 탐색

for m in range(19):                #세로 방향의 검은 돌이 5개 있는지 확인
    for n in range(19):
        if arr[n][m] == 1:
            cnt3 += 1
        else:
            if cnt3 == 5:
                result = 1
                grid.append(n - 5)
                grid.append(m)
            cnt3 = 0

cnt4 = 0 # 세로방향 하얀돌 탐색

for o in range(19):                #세로 방향의 하얀 돌이 5개 있는지 확인
    for p in range(19):
        if arr[p][o] == 2:
            cnt4 += 1
        else:
            if cnt4 == 5:
                result = 2
                grid.append(p - 5)
                grid.append(o)
            cnt4 = 0

cnt5 = 0 # 왼쪽 위에서  오른쪽 아래 대각선 검은돌 탐색
cnt6 = 0

for q in range(15):                #위에서 아래 대각선 검은돌 5개 있는지 확인
    for r in range(15):
        if q == r:
            if arr[q][r] == 1:
                cnt5 += 1
            else:
                if cnt5 == 5:
                    result = 1
                    grid.append(q - 5)
                    grid.append(r - 5)
                cnt5 = 0
        else:
            for s in range(5):
                if arr[q+s][r+s] == 1:
                    cnt6 += 1
                else:
                    if cnt6 == 5:
                        result = 1
                        grid.append(q)
                        grid.append(r)
                    cnt6 = 0

cnt7 = 0 # 왼쪽 위에서 오른쪽 아래 대각선 하얀돌 탐색
cnt8 = 0

for t in range(15):                #위에서 아래 대각선 하얀돌 5개 있는지 확인
    for u in range(15):
        if t == u:
            if arr[t][u] == 2:
                cnt7 += 1
            else:
                if cnt7 == 5:
                    result = 2
                    grid.append(t - 5)
                    grid.append(u - 5)
                cnt7 = 0
        else:
            for v in range(5):
                if arr[t+v][u+v] == 2:
                    cnt8 += 1
                else:
                    if cnt8 == 5:
                        result = 2
                        grid.append(t)
                        grid.append(u)
                    cnt8 = 0

cnt9 = 0 # 반대편 대각선 검은돌 탐색
cnt10 = 0

for w in range(18, 5, -1):
    for x in range(15):
        if w == x:
            if arr[w][x] == 1:
                cnt9 += 1
            else:
                if cnt9 == 5:
                    result = 1
                    grid.append(w - 5)
                    grid.append(x - 5)
                cnt9 = 0
        else:
            for y in range(5):
                if arr[w-y][x+y] == 1:
                    cnt10 += 1
                else:
                    if cnt10 == 5:
                        result = 1
                        grid.append(w-y - 5)
                        grid.append(x + y - 5)
                    cnt10 = 0

cnt11 = 0 # 반대편 대각선 하얀돌 탐색
cnt12 = 0

for z in range(18, 5, -1):
    for a in range(15):
        if z == a:
            if arr[z][a] == 2:
                cnt11 += 1
            else:
                if cnt11 == 5:
                    result = 2
                    grid.append(z - 5)
                    grid.append(a - 5)
                cnt11 = 0
        else:
            for b in range(5):
                if arr[z-b][a+b] == 2:
                    cnt12 += 1
                else:
                    if cnt12 == 5:
                        result = 2
                        grid.append(z-b - 5)
                        grid.append(a + b - 5)
                    cnt12 = 0

if result == 10:
    result = 0

print(result)
print(grid)