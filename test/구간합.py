import sys
sys.stdin = open('구간합.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    sum = [0]*N

    for i in range(N):
        
    maximum = max(sum[i])

    print('#{} {}'.format(tc, maximum))