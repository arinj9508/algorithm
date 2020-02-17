di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

arr = [list(map(int,input().split())) for _ in range(5)]
ans = 0
for i in range(5):
    for j in range(5):
       s = 0
       for k in range(4):
           ni = i + di[k] # k방향 이웃의 행
           nj = j + dj[k] # k방향 이웃의 열
           if 0<= ni <5 and 0 <= nj < 5 : # 유효한 인덱스인 경우
               s += abs(arr[i][j]-arr[ni][nj])
       ans += s
print(ans)