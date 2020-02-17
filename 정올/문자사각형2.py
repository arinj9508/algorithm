n = int(input())
A = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'*5000
arr = [[0]*n for _ in range(n)]

k = 0
for i in range(n):
    for j in range(n):
        if i % 2 ==0:
            arr[j][i] = A[k]
            k += 1
        else:
            arr[n-1-j][i] = A[k]
            k += 1

print(arr)