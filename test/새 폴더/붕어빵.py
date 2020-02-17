import sys
sys.stdin = open('붕어빵.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    A = list(map(int, input().split()))

    