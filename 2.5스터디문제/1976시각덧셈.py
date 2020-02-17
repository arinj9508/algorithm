import sys
sys.stdin = open('1976시각덧셈.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    time = list(map(int, input().split()))
    result = [0,0]

    result[0] = time[0] + time[2]
    result[1] = time[1] + time[3]

    if result[1] >= 60:
        result[1] = result[1] - 60
        result[0] += 1

    if result[0] >= 12:
        result[0] = result[0] - 12

    final = map(str, result)

    print('#{} {}'.format(tc, " ".join(final) ))
