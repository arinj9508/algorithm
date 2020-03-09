T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    mul = []
    for i in range(N-1):
        for j in range(i+1, N):
            if arr[i]*arr[j] > 10:
               mul.append(arr[i]*arr[j])

    mul.sort(reverse=True)

    for i in mul:
        tmp = str(i)
        result = 0
        for j in range(len(tmp)-1):
            if tmp[j] > tmp[j+1]:
                result = -1
                break

        if result != -1:
            result = tmp
            break
    print("#{} {}".format(tc, result))
