# 가위 1 바위 2 보 3
# def f(i,j):
#     if arr[i-1] == 1 and arr[j-1] == 3: # 가위 보
#         return i
#     elif arr[i-1] == 1 and arr[j-1] == 1: # 가위 가위
#         return i
#     elif arr[i-1] == 2 and arr[j-1] == 1: # 바위 가위
#         return i
#     elif arr[i-1] == 2 and arr[i-1] == 2: # 바위 바위
#         return i
#     elif arr[i-1] == 3 and arr[j-1] == 2: # 보 바위
#         return i
#     elif arr[i-1] == 3 and arr[j-1] == 3: # 보 보
#         return i
#     else:
#         return j
#
# def F(x, y):
#     if x == y:
#         return x
#     else:
#         a = F(x, (x+y)//2)
#         b = F((x+y)//2+1, y)
#         return f(a,b)
#
#
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     arr = list(map(int, input().split()))
#
#     print('#{} {}'.format(tc, F(1, N)))

def f(x, y):
    if arr[x-1] == 1 and arr[y-1] == 3:
        return x
    elif arr[x-1] == 1 and arr[y-1] == 1:
        return x
    elif arr[x-1] == 2 and arr[y-1] == 1:
        return x
    elif arr[x-1] == 2 and arr[y-1] == 2:
        return x
    elif arr[x-1] == 3 and arr[y-1] == 2:
        return x
    elif arr[x-1] == 3 and arr[y-1] == 3:
        return x
    else:
        return y

def F(start, end):
    if start == end:
        return start
    else:
    	a = F(start, (start+end)//2)
    	b = F((start+end)//2+1, end)
    	return f(a, b)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    print('#{} {}'.format(tc, F(1, N)))