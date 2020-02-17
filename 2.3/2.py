R,C = map(int,input().split())
arr2 = [list(map(int, input().split())) for _ in range(R)]
print(arr2)

# 행부터
for i in range(R):
    for j in range(C):
        print(arr2[i][j], end=' ')
    print()

# 열부터
for i in range(C):
    for j in range(R):
        print(arr2[j][i], end=' ')
    print()

# 마지막 행부터
for i in range(R-1, -1, -1):
    for j in range(C):
        print(arr2[i][j], end=' ')
    print()

# 마지막 열부터
for i in range(C-1, -1, -1):
    for j in range(R):
        print(arr2[j][i], end=' ')
    print()

# 마지막 행, 마지막 열부터
for i in range(R-1, -1, -1):
    for j in range(C-1, -1, -1):
        print(arr2[i][j], end=' ')
    print()