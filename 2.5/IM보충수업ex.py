N = int(input())
arr = list(map(int, input().split()))

sum_l = 0
sum_r = 0
for i in range(N):
    for j in range(1, arr[i]+1):
        if i + j < N - 1:
            sum_r += arr[i+j]
        if i - j >= 0:
            sum_l += arr[i-j]
    arr[i] = sum_r + sum_l

result = max(arr)
print(result)
