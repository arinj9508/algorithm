T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input()))
    # arr = input()
    result = []
    cnt = 0
    print(arr)
    for i in arr:
        if i == 1:
            cnt += 1
        else:
            result.append(cnt)
            cnt = 0

    result.append(cnt)


    # max_result = result[0]
    #
    # for j in range(1, len(result)):
    #     if max_result < result[j]:
    #         max_result = result[j]

    print('#{} {}'.format(tc, max(result)))