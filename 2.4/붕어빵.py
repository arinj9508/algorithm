import sys
sys.stdin = open('붕어빵.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    arr = list(map(int, input().split()))
    result = ['possible', 'Impossible']

    for i in range(len(arr)):
        if arr[i] < M:
            result = result[1]
            break
        else:
            continue

            for j in range()
            while arr[i] <=