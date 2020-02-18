T = int(input())
for tc in range(1, T+1):
    arr = list(map(str, input().split()))

    s = []
    result = []
    for i in range(len(arr)):
        if arr[i] == '.':
            if len(s) == 1:
                result.append(s.pop())
            else:
                result = ['error']
        elif arr[i] == '+':
            if len(s) >= 2:   # 스택에서 숫자가 2개 이상이 아닐 때의 경우를 고려
                n1 = s.pop()
                n2 = s.pop()
                s.append(int(n2) + int(n1))
            else:
                result = ['error']
                break
        elif arr[i] == '-':
            if len(s) >= 2:
                n1 = s.pop()
                n2 = s.pop()
                s.append(int(n2) - int(n1))
            else:
                result = ['error']
                break
        elif arr[i] == '*':
            if len(s) >= 2:
                n1 = s.pop()
                n2 = s.pop()
                s.append(int(n2) * int(n1))
            else:
                result = ['error']
                break
        elif arr[i] == '/':
            if len(s) >= 2:
                n1 = s.pop()
                n2 = s.pop()
                s.append(int(n2) // int(n1))
            else:
                result = ['error']
                break
        else:
            s.append(arr[i])

    print('#{} {}'.format(tc, "".join(map(str,result))))