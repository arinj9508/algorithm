import sys
sys.stdin = open('붕어빵.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = [0] * (max(A) + 1)
    result = ['Possible', 'Impossible']

    for x in A:  # 카운트배열 생성
        B[x] += 1

    for i in range(1, len(B)):  # 누적 합을 저장
        B[i] += B[i - 1]  # 자신과 왼쪽까지 누적된 합을 더함

    for j in range(len(A)):