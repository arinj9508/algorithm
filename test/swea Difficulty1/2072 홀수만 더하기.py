import sys
sys.stdin = open('홀수만 더하기.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    arr = list(map(int, input().split()))
    result = 0
    for i in range(len(arr)):
        result += 

    print('#{} {}'.format(tc, result))