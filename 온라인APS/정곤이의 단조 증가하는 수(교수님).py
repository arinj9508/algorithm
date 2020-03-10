T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
# N개의 값들에서 2개 선택해서 곱하는 모든 경우
    ans = -1
    for i in range(N-1):
        for j in range(i+1, N):
            num = arr[i] * arr[j]
            if ans >= num:
                break

            t = num
            b = t % 10
            t //= 10
            while t:
                a = t % 10
                if a > b:
                    break
                t //= 10
                b = a # 단조증가하는 수
            else:
                ans = max(ans, num)

    print(ans)