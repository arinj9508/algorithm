n = int(input())
arr = [[0]*n for _ in range(n)]
alphabet = 'ABCDEFGHIJKLMNOP'
k = 0
for i in range(n):
    for j in range(n):
        arr[n-1-j][n-1-i] = alphabet[k]
        k += 1

for k in arr:
    print("".join(map(str, k)))