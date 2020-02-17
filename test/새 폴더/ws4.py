import sys
sys.stdin = open('input4.txt', 'r')

T = int(input())

for tc in range(1,T+1):
    K,N,M = map(int, input().split())
    C = list(map(int, input().split()))
    L = [0]*(N+1)
    for i in range(len(C)):
        L[(C[i])] +=1
    go = K
    count = 0
    while go < N:
        while L[go] == 0:
            go -= 1
        count += 1
        go += K

        if count > N:
            break

    if count >= N:
        print('#{} {}'.format(tc, '0'))

    else:
        print('#{} {}'.format(tc, count))
