# T = int(input())
# for tc in range(1, T + 1):
#     N, M = map(int, input().split())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#     maxtotal = 0
#     for i in range(N):
#         for j in range(M):
#             total = 0
#             for k in range(1, arr[i][j] + 1):
#
#                 if 0 <= i - k:
#                     total += arr[i - k][j]
#                 if i + k < N:
#                     total += arr[i + k][j]
#                 if 0 <= j - k:
#                     total += arr[i][j - k]
#                 if j + k < M:
#                     total += arr[i][j + k]
#
#             total += arr[i][j]
#             if total > maxtotal:
#                 maxtotal = total
#     print('#{} {}'.format(tc, maxtotal))

# 예원이 풀이 (4배열 상하좌우로 푼거)
T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    result = []
    sum = 0
    for x in range(len(arr)):
        for y in range(len(arr[x])):
            sum = 0
            for z in range(1, arr[x][y] + 1):
                for i in range(4):
                    test_x = x + dx[i] * z
                    test_y = y + dy[i] * z
                    if 0 <= test_x < N and 0 <= test_y < M:
                        sum += arr[test_x][test_y]
            sum += arr[x][y]
            result.append(sum)

    print('#{} {}'.format(tc, max(result)))


# T = int(input())
# for tc in range(1, T + 1):
#     N, M = map(int, input().split())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#
#     max_total = 0
#     for x in range(N):
#         for y in range(M):
#             total = 0
#             for i in range(-(arr[x][y]), (arr[x][y]) + 1):
#                 for j in range(-(arr[x][y]), (arr[x][y]) + 1):
#                     if i == 0:
#                         if 0 <= x + i < N and 0 <= y + j < M:
#                             total += arr[x + i][y + j]
#                     if j == 0:
#                         if 0 <= x + i < N and 0 <= y + j < M:
#                             total += arr[x + i][y + j]
#             total -= arr[x][y]
#             if total > max_total:
#                 max_total = total
#
#     print('#{} {}'.format(tc, max_total))