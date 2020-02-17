
N, M, K = map(int, input().split())
arr = list(map(int, input().split()))
result = ['possible', 'Impossible']

for i in range(len(arr)):
    if arr[i] < M:
        result = result[1]

print(result)


