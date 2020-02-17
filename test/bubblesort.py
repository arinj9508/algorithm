def bubble(a):
    for i in range(len(a)-1, 0, -1): # 구간 끝 감소
        for j in range(0, i): # 오른쪽 원소가 존재하는 범위
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
    return a

a = [7, 4, 3, 2, 5, 4]
a = bubble(a)
print(a)

# a = [1,5,4,4,2]
# n = 5
#
# for i in range(n):
#     for j in range(n-1-i):
#         if a[j] > a[j+1]:
#             a[j], a[j+1] = a[j+1], a[j]
#
# print(a)