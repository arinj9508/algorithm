p = "is"
t = "this is a book~!"
M = len(p)
N =len(t)

def BruteForce(p,t):
    i = 0
    j = 0
    while j < M and i < N:
        if t[i] != p[j]:
            i = i - j # 출발지로 되돌림
            j = -1 # 출발지 이전으로
        i = i + 1 # 다음 칸
        j = j + 1 # pattern의 맨 앞
    if j == M:
        return i - M # 검색성공
    else:
        return -1 # 검색실패