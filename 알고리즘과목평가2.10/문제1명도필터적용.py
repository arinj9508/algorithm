T = int(input())
for tc in range(1, T+1):
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    arr = [list(map(int, input().split())) for _ in range(10)]

    A_sum_before = 0
    B_sum_before = 0
    A_sum_after = 0
    B_sum_after = 0
    for i in range(A[0], A[2]+1):
        for j in range(A[1], A[3]+1):
            A_sum_before += arr[i][j]
            if (arr[i][j])*2 >= 255:
                A_sum_after += 255
            else:
                A_sum_after += (arr[i][j])*2

    for k in range(B[0], B[2]+1):
        for l in range(B[1], B[3]+1):
            B_sum_before += arr[k][l]
            B_sum_after += (arr[k][l])//2

    result1 = A_sum_after - A_sum_before
    result2 = B_sum_before - B_sum_after
    final = result1 + result2

    print('#{} {}'.format(tc, final))
