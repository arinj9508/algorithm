import sys
sys.stdin = open('다이아몬드.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    text = list(map(str, input()))
    result = [['.']*(4*len(text)+1)for _ in range(5)]

    for i in range(5):
        for j in range(4*len(text)+1):
            if i % 2:
                if j % 2 != 0:
                    result[i][j] = '#'
        if i == 0 or i == 4:
            for k in range(len(text)):
                result[i][4*(k+1)-2] = '#'
        if i == 2:
            for l in range(len(text)+1):
                result[i][4*l] = '#'
            for m in range(len(text)):
                result[i][4*m+2] = text[m]

    for kitti in result:
        print("".join(map(str, kitti)))