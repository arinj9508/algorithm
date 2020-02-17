import sys
sys.stdin = open('input.1.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    count1 = 1
    count2 = 1

    for i in range(len(arr)-1):
        if arr[i+1] > arr[i]:
            count1 += 1
        if arr[i+1] < arr[i]:
            count2
    num = max(count1, count2)

    print('#{} {}'.format(tc, num))