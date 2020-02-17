import sys
sys.stdin = open('input5.txt', 'r')

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    carrot = list(map(int, input().split()))
    comparison = [1] * N
    i = 0
    for i in range(N-1):
        if carrot[i]<carrot[i+1]:
            comparison[i+1] = comparison[i]+1
        else:
            comparison[i+1] = 1
    print('#{} {}'.format(tc, max(comparison)))




    # while i < N:
    #     carrot[i]<carrot[i+1]
    #     cnt += 1
    #
    # print(cnt)

