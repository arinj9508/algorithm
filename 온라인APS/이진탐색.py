def binary_search(n, k):
    start = 1
    end = k

    cnt = 1
    while start <= end:
        midpoint = (start + end)//2
        if midpoint == n:
            return cnt
        elif midpoint > n:
            end = midpoint
            cnt += 1
        else:
            start = midpoint
            cnt += 1

T = int(input())
for tc in range(1, T+1):
    P, Pa, Pb = map(int, input().split())

    A = binary_search(Pa,P)
    B = binary_search(Pb,P)

    result = 0
    if A < B:
        result = 'A'
    elif A > B:
        result = 'B'
    else:
        result = 0

    print("#{} {}".format(tc, result))