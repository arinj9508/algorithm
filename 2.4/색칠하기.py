import sys
sys.stdin = open('색칠하기.txt', 'r')


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    info = [list(map(int, input().split())) for _ in range(N)]
    cnt = 0
    arr = [[0] * 10 for _ in range(10)]  # 초기화 되는 위치를 꼭 확인

    for i in range(N):
        for k in range(info[i][0], info[i][2]+1):
            for l in range(info[i][1], info[i][3]+1):
                if arr[k][l] != info[i][4]:
                    arr[k][l] += info[i][4]

    for j in range(10):
        for h in range(10):
            if arr[j][h] == 3:
                cnt += 1

    print('#{} {}'.format(tc, cnt))



