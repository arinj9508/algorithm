import sys
sys.stdin = open('2.4hw.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    arr1 = list(map(int, input().split()))
    arr2 = [[0]*2 for _ in range(n)]

    for i in range(n):
        for j in range(2):
            arr2[i][j] = arr1[2 * i + j]

    arr3 =[]  # 2차원 배열에서 열의 숫자만 뺀 리스트
    for k in range(n):
        arr3.append(arr2[k][1])

    arr4 = [] # 결과를 낼 리스트
    for h in range(n):
        if arr2[h][0] not in arr3:
            arr4.append(arr2[h][0])
            arr4.append(arr2[h][1])

    for p in range(n): # arr4에서 연결 횟수
        for d in range(n): # arr2에서 행의 갯수만큼 찾아볼 횟수
            if arr2[d][0] == arr4[-1]:
                arr4.append(arr2[d][0])
                arr4.append(arr2[d][1])
    arr5 = map(str,arr4)

    print('#{} {}'.format(tc, " ".join(arr5)))






