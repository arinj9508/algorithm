# 반복을 이용
def maze_runner(cur_x, cur_y):
    stack = [(cur_x, cur_y)]            # stack에 현재 위치 추가
    while stack:                            # stack에 위치 정보가 남아 있는 경우 반복
        cur_x, cur_y = stack.pop()      # 가장 최근에 가지 않은 위치로 이동
        if Maze_list[cur_x][cur_y] == 3:   # 해당 위치가 3(도착점) 일 경우
            return 1
        Maze_list[cur_x][cur_y] = 1     # 방문한 곳을 1로 채워버림
        for i in range(4):                  # 주변 4방향에 대해서
            temp_x = cur_x + dir_list[i][0]
            temp_y = cur_y + dir_list[i][1]
            if Maze_list[temp_x][temp_y] != 1:  # 만약 막혀있는 곳이 아니라면
                stack.append((temp_x, temp_y))  # 스택에 방문 안 한곳으로 추가 - 가장 마지막에 추가한 곳이 다음 방문하게 될 것
    return 0                                    # stack에 아무것도 없으면 안 간곳이 없음 -> 0을 리턴
for _ in range(10):
    t = int(input())
    Maze_list = [list(map(int, list(input()))) for _ in range(16)]
    for x in range(16):                     # 시작점 찾기
        for y in range(16):
            if Maze_list[x][y] == 2:
                cur_x, cur_y = x, y
    dir_list = ((-1, 0), (1, 0), (0, -1), (0, 1))
    print('#{0} {1}'.format(t, maze_runner(cur_x, cur_y)))


# 재귀를 이용한 미로1
def maze_runner(cur_x, cur_y):
    if Maze_list[cur_x][cur_y] == 3:    # 지금 위치가 도착점일 경우 1 리턴
        return 1
    visited.append((cur_x, cur_y))  # 지금 위치를 방문했다고 표시함
    for i in range(4):              # 주변 4방향 탐색
        temp_x = cur_x + dir_list[i][0]
        temp_y = cur_y + dir_list[i][1]
        if Maze_list[temp_x][temp_y] != 1 and (temp_x, temp_y) not in visited:      # 만약 해당 위치가 벽이 아니고, 방문 X라면
            if maze_runner(temp_x, temp_y):     # 해당 위치로 이동해서 탐색 ㄱㄱ
                return 1
    return 0
for _ in range(10):
    t = int(input())
    Maze_list = [list(map(int, list(input()))) for _ in range(16)]
    for x in range(16):
        for y in range(16):
            if Maze_list[x][y] == 2:
                cur_x, cur_y = x, y
    dir_list = ((-1, 0), (1, 0), (0, -1), (0, 1))
    visited = []
    print('#{0} {1}'.format(t, maze_runner(cur_x, cur_y)))





