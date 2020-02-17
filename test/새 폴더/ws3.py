import sys
sys.stdin = open('input3.txt', 'r')

T = int(input())

for tc in range(1,T+1):
    N, M = map(int, input().split())
    a = list(map(int, input().split()))
    max_sum = []
    min_sum = []
    for i in range(0,N-M+1):
        max_sum.append(sum(a[i:i+M]))
        min_sum.append(sum(a[i:i+M]))
    result = max(max_sum) - min(min_sum)
    print('#{} {}'.format(tc, result))


    # print('#{} {}'.format(tc,a))
    # max_sum = 0
    # for x in range(N):
    #     for i in range(M):
    #         max_
