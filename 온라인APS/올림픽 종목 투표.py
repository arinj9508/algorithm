T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    result = []
    final = []
    for i in B:
        for j in range(len(A)):
            if i >= A[j]:
                result.append(j+1)
        final.append(min(result))
        del result[:]

    final_cnt = dict()
    for num in final:
        if num not in final_cnt.keys():
            final_cnt[num] = 1
        else:
            final_cnt[num] += 1

    max_value = max(final_cnt.values())
    ans = 0
    for key, value in final_cnt.items():
        if value == max_value:
            ans = key

    print("#{} {}".format(tc, ans))
