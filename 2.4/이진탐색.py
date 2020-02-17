import sys
sys.stdin = open('이진탐색.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    P, A, B = list(map(int, input().split()))

    def binarySearch()