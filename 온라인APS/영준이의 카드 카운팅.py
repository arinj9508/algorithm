T = int(input())
for tc in range(1, T+1):
    arr = list(input())

    result = [13, 13, 13, 13]
    cards = []
    for i in range(0, len(arr), 3):
        tmp = arr[i: i+3]
        cards.append(tmp)

    for i in range(len(cards)-1):
        for j in range(i+1,len(cards)):
            if cards[i] == cards[j]:
                result = 'ERROR'

    if result != 'ERROR':
        for j in range(len(cards)):
            if cards[j][0] == 'S':
                result[0] -= 1
            elif cards[j][0] == 'D':
                result[1] -= 1
            elif cards[j][0] == 'H':
                result[2] -= 1
            else:
                result[3] -= 1

    if result != 'ERROR':
        result = " ".join(map(str,result))

    print("#{} {}".format(tc, result))


