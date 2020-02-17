import sys
sys.stdin = open('백만장자프로젝트.txt'. 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    total_profit = 0  #총이득
    top_price = arr[N-1] #마지막 날의 가격으로 최고가 초기화

    for i in range(N-1, -1, -1): #뒤에서부터 순회
        if arr[i] < top_price:
            total_profit += top_price - arr[i]
        else:
            top_price = arr[i]

    print('#{} {}'.format(tc, total_profit))