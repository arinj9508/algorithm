N = int(input())   # 10 <= N <= 1000

lst = []
for i in range(1, N+1):
    if i // 10 == 3 or i // 10 == 6 or i // 10 == 9:
        if i % 10 == 3 or i % 10 == 6 or i % 10 == 9:
            lst.append('--')
        else:
            lst.append('-')
    else:
        if i % 10 == 3 or i % 10 == 6 or i % 10 == 9:
            lst.append('-')
        else:
            lst.append(i)

print(" ".join(map(str,lst)))
