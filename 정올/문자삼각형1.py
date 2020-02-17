n = int(input())
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'*5000
arr = [[0]*n for _ in range(n)]

for i in range(n):
    for j in range(n):
