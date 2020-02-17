import sys
sys.stdin = open('주말과제.txt', 'r')

def bubble(arr):
    for i in range(len(arr) - 1, 0, -1):  # 구간 끝 감소
        for j in range(0, i):  # 오른쪽 원소가 존재하는 범위
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    arr = list(map(int, input().split()))
    arr = bubble(arr)
    result = ['Possible', 'Impossible']
    for x in range(1, len(arr)):
        if arr[0] >= M:
            if arr[x] >= M * (x + 1):
                answer = result[0]
            else:
                result = result[1]
        else:
            result = result[1]

    print('#{} {}'.format(tc, result))
