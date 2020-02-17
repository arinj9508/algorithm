import sys
sys.stdin = open('의석이의 세로로 말해요.txt','r')

T = int(input())
for tc in range(1, T+1):
    arr = [list(map(str, input()))for _ in range(5)]

    for i in arr:
        print("".join(i))

    for a in range(5):
        for b in range():


    # a = list(map(str, input()))
    # b = list(map(str, input()))
    # c = list(map(str, input()))
    # d = list(map(str, input()))
    # e = list(map(str, input()))
    #
    # result = []
    # for i in range(len(a)):
    #     result.append(a[i])
    #     for j in range(len(b)):
    #         if j == i:
    #             result.append(b[j])
    #             for k in range(len(c)):
    #                 if k == i:
    #                     result.append(c[k])
    #                     for l in range(len(d)):
    #                         if l == i:
    #                             result.append(d[l])
    #                             for m in range(len(e)):
    #                                 if m == i:
    #                                     result.append(e[m])
    #
    # print('#{} {}'.format(tc, "".join(result)))