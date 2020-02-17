import sys
sys.stdin = open('1966숫자를정렬하자.txt', 'r')


def bubble(a):
    for i in range(len(a) - 1, 0, -1):  # 구간 끝 감소
        for j in range(0, i):  # 오른쪽 원소가 존재하는 범위
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    return a

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    a = list(map(int, input().split()))
    b = bubble(a)
    c = map(str, b)

    print('#{} {}'.format(tc, " ".join(c)))
