import sys
sys.stdin = open('flatten.txt', 'r')

T = 10
for tc in range(10):
    N = int(input())
    arr = list(map(int, input().split()))
