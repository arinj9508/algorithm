T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    max_length = max(len(A), len(B))
    if max_length == len(A):
        D = A
    elif max_length == len(B):
        D = B

    if len(A) <= len(B):
        C = A
    else:
        C = B

    Multi = []
    for i in range(len(D) - len(C) + 1):
        mul_sum = 0
        for j in range(len(C)):
            mul = D[i+j]*C[j]
            mul_sum += mul
        Multi.append(mul_sum)

    print('#{} {}'.format(tc, max(Multi)))
