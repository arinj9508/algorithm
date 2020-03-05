import sys
sys.stdin = open('붕어빵.txt','r')

T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int,input().split())
    arr = list(map(int, input().split()))

    for i in range(N):
        if arr[i] < M:
            result = 'Impossible'
        else:
            result = 'Possible'

    fish = 0
    for j in range(11112):
        if result != 'Impossible':
            if j != 0:
                if j % M == 0:
                    fish += K
            if j in arr:
                cnt = 0
                for k in range(len(arr)):
                    if arr[k] == j:
                        cnt += 1
                fish -= cnt
                if fish < 0:
                    result = 'Impossible'
                else:
                    result = 'Possible'

    print('#{} {}'.format(tc, result))

