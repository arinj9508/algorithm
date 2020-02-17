T = int(input())
for tc in range(1, T+1):
    N = list(map(str, input()))
    M = list(map(str, input()))

    alphabet = {}
    k = 0
    for i in range(len(N)):                    # str1에 들어있는 알파벳을 딕셔너리로 만들기
        if N[i] not in alphabet.values():
            alphabet[k] = N[i]
            k += 1

    result = {}
    for x in M:
        for y in range(len(alphabet)):
            if x == alphabet[y]:
                if x not in result.keys():
                    result[x] = 1
                else:
                    result[x] += 1

    print('#{} {}'.format(tc, max(result.values())))