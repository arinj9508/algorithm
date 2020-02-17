a = [1, 5, 7]
for i1 in range(3):
    for i2 in range(3):
        if i1 != i2:
            for i3 in range(3):
                if i3 != i1 and i3 != i2:
                    print(a[i1], a[i2], a[i3])

# for i1 in range(1, 4):
#     for i2 in range(1, 4):
#         if i1 != i2:
#             for i3 in range(1, 4):
#                 if i3 != i1 and i3 != i2:
#                     print(i1, i2, i3)