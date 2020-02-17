T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))



print('#{} {} {}'.format(tc, maxIdx+1, arr[maxIdx]))