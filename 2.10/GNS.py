number = {0: 'ZRO', 1: 'ONE', 2: 'TWO', 3: 'THR', 4: 'FOR', 5: 'FIV', 6: 'SIX', 7: 'SVN', 8: 'EGT', 9: 'NIN'}

T = int(input())
for tc in range(1, T+1):
    tcn, N = map(str, input().split())
    N = int(N)
    arr = list(map(str, input().split()))

    result = []
    for i in range(len(number)):
        for j in arr:
            if j == number[i]:
                result.append(j)

    print('#{}'.format(tc))
    print(" ".join(result))