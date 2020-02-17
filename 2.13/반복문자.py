# def f(n, k):
#     if 0 <= n+1 < k:
#         if arr[n] == arr[n+1]:
#             arr.pop(arr[n])
#             arr.pop(arr[n+1])
#         else:
#             f(n+1, k)
#     print(len(arr))

T = int(input())
for tc in range(1, T+1):
    arr = list(input())
    s = ['1']

    for i in range(len(arr)):
        if arr[i] != s[-1]:
            s.append(arr[i])
        else:
            s.pop()


    print('#{} {}'.format(tc, len(s)-1))