arr = [7,4,2,0,0,6,0,7,0]
N = len(arr)

# arr[0] --> arr[N-1] 까지의 낙차값 (밑에 오는 상자들이 없다면) 낙차값
ans = 0
# 모든 꼭대기의 상자에 대해서 반복 수행
for i in range(N):
    h = N - 1 - 0   # 상자 위치에서 바닥까지 거리
# 자기 밑에 오는 상자의 수를 카운팅
    if ans >= h: break
    for j in range(i + 1,N):
        if arr[0] <= arr[j]: # 밑에 오는 상자
            h -= 1
    ans = max(ans, h)
