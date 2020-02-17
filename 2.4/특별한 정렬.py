import sys
sys.stdin = open('특별한 정렬.txt', 'r')


def bubble(A):
    for i in range(len(A) - 1, 0, -1):
        for j in range(0, i):
            if A[j] > A[j + 1]:
                A[j], A[j + 1] = A[j + 1], A[j]
    return A

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    A = list(map(int, input().split()))
    A = bubble(A)
    B = [0]*10

    for k in range(5):
        B[(2*k) + 1] = A[k]
        B[2 * k] = A[N-k-1]
    BB = map(str,B)

    print('#{} {}'.format(tc, " ".join(BB)))