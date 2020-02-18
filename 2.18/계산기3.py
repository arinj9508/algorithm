for tc in range(1, 11):
    N = int(input())
    arr = list(input())

    s = []
    need = []
    for i in range(len(arr)):
        if arr[i] == '(':
            s.append(i)
        elif arr[i] == ')':
            while s[-1] == '(':
                
        elif arr[i] == '+':

        elif arr[i] == '-':

        elif arr[i] == '*':

        elif arr[i] == '/':

        else:
            need.append(i)