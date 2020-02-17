import sys
sys.stdin = open('숫자카드.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    A = list(map(int, input()))
    B = [0] * 10

    for x in A:  # 카운트배열 생성
        B[x] += 1
    # print(B)
    maximum = 0
    index = 0

    for i in range(len(B)):
        if index <= B[i]:
            index = B[i]
            maximum = i
        # print(maximum, index)


    print('#{} {} {}'.format(tc, maximum , index))
