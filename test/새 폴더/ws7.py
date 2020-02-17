import sys
sys.stdin = open('input6.txt', 'r')

T= 10

for tc in range(1,11):
    dump = int(input())
    height = list(map(int, input().split()))

    for i in range(dump):
        maxh_idx = height.index(max(height))
        minh_idx = height.index(min(height))
        height[maxh_idx] -= 1
        height[minh_idx] +=1

        result = max(height) - min(height)
    print('#{} {}'.format(tc, result))










    # for x in range(len(height)):
    #     if height[x] >= h:
    #         h = height[x]
    #     else:
    #         h = h
    # print('#{} {}'.format(tc, h))


# print('#{} {}'.format(tc, height))


# while dump = 0
#     for x in range(len(height)):
#         if height[x] >= max_height:
#             max_height = height[x]
#           else:
#             max_height = max_height
#     for x in range(len(height)):
#         if height[x] =< min_height:
#             max_height = height[x]
#         else:
#             min_height = min_height
#     print('#{} {} {}'.format(tc, max_height, min_height))