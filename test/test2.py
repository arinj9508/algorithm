import sys
sys.stdin = open('input.1.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    cp = [1]*N
    i = 0

    for i in range(len(arr)-1):
        if arr[i+1] > arr[i]:
            cp[i+1] = cp[i]+1
        else:
            cp[i+1]=1

    print('#{} {}'.format(tc, max(cp)))