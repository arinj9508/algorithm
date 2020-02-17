T = int(input())
for tc in range(1, T+1):
    arr = list(input())

    s = []
    result = 2
    for i in range(len(arr)):
        if arr[i] == '{' or arr[i] == '(':
            s.append(arr[i])
        if arr[i] == ')':
            if len(s) == 0:    # ★ 스택에서 괄호가 아무것도 없을 때의 경우를 고려해야 한다!! ex) (())) 인 경우
                result = 0
                break
            if s[-1] == '(':
                s.pop()
            else:
                result = 0
        if arr[i] == '}':
            if len(s) == 0:
                result = 0
                break
            if s[-1] == '{':
                s.pop()
            else:
                result = 0

    if len(s) != 0:
        result = 0
    if result != 0:
        result = 1

    print('#{} {}'.format(tc, result))