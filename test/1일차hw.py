import sys
sys.stdin = open('input.hw.txt', 'r')

T = 10 # 테스트 케이스 10으로 지정
for tc in range(1, T+1): # 10번의 테스트 케이스 동안
    N = int(input()) # 가로의 길이를 입력해줌
    arr = list(map(int, input().split())) # 각 리스트의 크기를 지정
    apt = 0  # apt는 조망권을 확보한 아파트 수
    for i in range(2, N-1): # 마지막 가로의 길이까지
        if arr[i] > arr[i-2] and arr[i] > arr[i-1] and arr[i] > arr[i+1] and arr[i] > arr[i+2]:
            max_height = max(arr[i-2],arr[i-1],arr[i+1],arr[i+2])
            apt += (arr[i] - max_height)
    print('#{} {}'.format(tc, apt))