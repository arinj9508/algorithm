T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = str(input())

    result = [0]*10
    for i in arr:
        if i == '0':
            result[0] += 1
        elif i == '1':
            result[1] += 1
        elif i == '2':
            result[2] += 1
        elif i == '3':
            result[3] += 1
        elif i == '4':
            result[4] += 1
        elif i == '5':
            result[5] += 1
        elif i == '6':
            result[6] += 1
        elif i == '7':
            result[7] += 1
        elif i == '8':
            result[8] += 1
        else:
            result[9] += 1

    final = max(result)
    index = []
    for i in range(len(result)):
        if result[i] == final:
            index.append(i)
    final_index = max(index)

    print("#{} {} {}".format(tc, final_index, final))