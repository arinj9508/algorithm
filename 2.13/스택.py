# 스택

s = [0]*10
top = -1

top += 1 # push(10)
s[top] = 10

top += 1 # push(20)
s[top] = 20

if top != -1:
    d = s[top] # pop()
    top -= 1
    print(d)



stack = []
stack.append(100)
stack.append(200)
stack.append(300)
while len(stack) != 0:
    print(stack.pop())  # 뒤에서 부터 꺼낸다.(last in first out)


# 반복문 안에 함수를 호출하는 것이 제일 비효율적.


# 처리할 인덱스가 배열의 크기와 같아지면(배열을 벗어나면) 중단

# 재귀호출

def f(n,k): # n은 복사할 인덱스, k는 배열의 크기
    if n == k:
        print(B)
        return #생략도 가능
    else: # 복사할 원소가 있으면
        B[n] = A[n]
        f(n+1, k) # 다음 원소를 복사하러 이동
    # return  생략가능

# 재귀함수로 A배열 원소를 배열B에 복사
A = [1,2,3]
B = [0]*3
f(0,len(A))



def f(n,k): # n은 복사할 인덱스, k는 배열의 크기
    global maxV   # 전역변수
    if n == k:
        return # 이때는 비워있으면 안되니깐 return 써 놓기!
    else: # 복사할 원소가 있으면
        if maxV < A[n]:
            maxV = A[n]
            print(maxV)
            f(n+1, k)
    # return
A = [1,2,3]
maxV = 0
f(0,len(A))


# 원하는 조건을 찾으면 중단하는 경우
def f(n,k,v):
    if n == k: # 배열을 벗어나면
        return 0 # 찾는 값이 배열에 없으면
    elif A[n]==v: # 원하는 값 v를 찾으면
        return 1 # v가 있으면
    else: # 배열을 벗어나지 않았고, 값 v를 못 찾았으면
        return f(n+1, k,v) #다음 원소를 확인하러 이동

A = [1,2,3,7,5,4,9,8]
print(f(0, len(A), 7))
print(f(0, len(A), 10))



# DP(Dynamic Programming)
# 피보나치 수 DP 적용 알고리즘

n = 10
fibo = [0]*(n+1)
fibo[0] = 0
fibo[1] = 1
for i in range(2, n+1):
    fibo[i] = fibo[i-1] + fibo[i-2]
print(fibo)


# DP를 이용한 팩토리얼 계산
#memoization == 하향식DP

n=10
fact = [0]*(n+1)
fact[0] = 1
fact[1] = 1
for i in range(2, n+1):
    fact[i] = i*fact[i-1]
print(fact)


# 연습문제 : {1,2,3}의 모든 부분 집합 출력하기

def f(n,k):
    if n == k: # 부분집합 중 1개 완성
        for i in range(k):
            if L[i] ==1:
                print(A[i], end=' ')
        print()
        return
    else:
        L[n] = 0
        f(n+1, k)
        L[n] = 1
        f(n+1, k)

A = [1,2,3]
L = [0]*3
f(0,3)


# DFS(깊이우선탐색)

# 무향그래프 : Edge의 방향이 없는 경우

V = 5
E = 6

read V,E

for i in range( 1, E+1):
    read n1, n2;
    M[n1][n2] = 1;
    M[n2][n1] = 1;


# 재귀를 사용한 DFS(깊이우선탐색)

DFS(n)
    V[n] = 1  # 방문 표시
    visit(n)  # 노드에 대해 처리할 일
    for i : 1 -> N   # 인접 행렬 n행 검색
        if( M[n][i] != 0 & V[i] == 0 ):
            DFS(i)  # 인접하고 방문하지 않은 노드로 이동


# DFS 연습문제
# Input
# 5 6
# 1 2 1 3 3 2 2 5 3 4 5 4

def dfs(n, V):
    visited[n] = 1 # n번 노드에 방문 표시
    print(n, end=' ') # n번 노드에서 할 일
    for i in range(1,V+1): # 모든 노드 i에 대해
        if adj[n][i] == 1 and visited[i] == 0: # n에 인접하고, 방문하지 않았으면
            dfs(i, V) # i노드로 이동


# 인접행렬 생성
V, E = map(int, input().split())
adj = [[0]*(V+1) for _ in range(V+1)]
edge = list(map(int, input().split()))
visited = [0]*(V+1)
for i in range(E):
    n1 = edge[i*2]
    n2 = edge[i*2+1]
    adj[n1][n2] = 1
    # adj[n2][n1] = 1 # 방향성이 없는 무향그래프인 경우

for i in range(V+1):
    for j in range(V+1):
        if i != 0 and j != 0:
            print(adj[i][j], end=' ')
    print()

print()
dfs(1, V)


# 반복구조 dfs는 지나온 노드를 스택에 저장하거나, 방문하지 않고 남겨놓은 노드를 스택에 저장

def dfs2(n, V): # 반복구조의 dfs
    s = [] # 스택 생성
    used = [0]*(V+1) # 중복확인
    s.append(n) # push(n) 시작점 저장
    used[n] = 1
    while len(s) != 0: # 스택이 비어있지 않으면
        n = s.pop() # pop()
        print(n, end=' ')
        for i in range(1, V+1):
            if adj[n][i] ==1 and used[i] == 0: # i가 인접이고, 스택에 들어있지 않으면,
                s.append(i) # 인접 목록 추가
                used[i] = 1 # 목록에 추가 표시


# 인접행렬 생성
V, E = map(int, input().split())
adj = [[0]*(V+1) for _ in range(V+1)]
edge = list(map(int, input().split()))
visited = [0]*(V+1)
for i in range(E):
    n1 = edge[i*2]
    n2 = edge[i*2+1]
    adj[n1][n2] = 1
    # adj[n2][n1] = 1 # 방향성이 없는 무향그래프인 경우

dfs2(1, V)                                                   # 스택

s = [0]*10
top = -1

top += 1 # push(10)
s[top] = 10

top += 1 # push(20)
s[top] = 20

if top != -1:
    d = s[top] # pop()
    top -= 1
    print(d)



stack = []
stack.append(100)
stack.append(200)
stack.append(300)
while len(stack) != 0:
    print(stack.pop())  # 뒤에서 부터 꺼낸다.(last in first out)


# 반복문 안에 함수를 호출하는 것이 제일 비효율적.


# 처리할 인덱스가 배열의 크기와 같아지면(배열을 벗어나면) 중단

# 재귀호출

def f(n,k): # n은 복사할 인덱스, k는 배열의 크기
    if n == k:
        print(B)
        return #생략도 가능
    else: # 복사할 원소가 있으면
        B[n] = A[n]
        f(n+1, k) # 다음 원소를 복사하러 이동
    # return  생략가능

# 재귀함수로 A배열 원소를 배열B에 복사
A = [1,2,3]
B = [0]*3
f(0,len(A))



def f(n,k): # n은 복사할 인덱스, k는 배열의 크기
    global maxV   # 전역변수
    if n == k:
        return # 이때는 비워있으면 안되니깐 return 써 놓기!
    else: # 복사할 원소가 있으면
        if maxV < A[n]:
            maxV = A[n]
            print(maxV)
            f(n+1, k)
    # return
A = [1,2,3]
maxV = 0
f(0,len(A))


# 원하는 조건을 찾으면 중단하는 경우
def f(n,k,v):
    if n == k: # 배열을 벗어나면
        return 0 # 찾는 값이 배열에 없으면
    elif A[n]==v: # 원하는 값 v를 찾으면
        return 1 # v가 있으면
    else: # 배열을 벗어나지 않았고, 값 v를 못 찾았으면
        return f(n+1, k,v) #다음 원소를 확인하러 이동

A = [1,2,3,7,5,4,9,8]
print(f(0, len(A), 7))
print(f(0, len(A), 10))



# DP(Dynamic Programming)
# 피보나치 수 DP 적용 알고리즘

n = 10
fibo = [0]*(n+1)
fibo[0] = 0
fibo[1] = 1
for i in range(2, n+1):
    fibo[i] = fibo[i-1] + fibo[i-2]
print(fibo)


# DP를 이용한 팩토리얼 계산
#memoization == 하향식DP

n=10
fact = [0]*(n+1)
fact[0] = 1
fact[1] = 1
for i in range(2, n+1):
    fact[i] = i*fact[i-1]
print(fact)


# 연습문제 : {1,2,3}의 모든 부분 집합 출력하기

def f(n,k):
    if n == k: # 부분집합 중 1개 완성
        for i in range(k):
            if L[i] ==1:
                print(A[i], end=' ')
        print()
        return
    else:
        L[n] = 0
        f(n+1, k)
        L[n] = 1
        f(n+1, k)

A = [1,2,3]
L = [0]*3
f(0,3)


# DFS(깊이우선탐색)

# 무향그래프 : Edge의 방향이 없는 경우

V = 5
E = 6

read V,E

for i in range( 1, E+1):
    read n1, n2;
    M[n1][n2] = 1;
    M[n2][n1] = 1;


# 재귀를 사용한 DFS(깊이우선탐색)

DFS(n)
    V[n] = 1  # 방문 표시
    visit(n)  # 노드에 대해 처리할 일
    for i : 1 -> N   # 인접 행렬 n행 검색
        if( M[n][i] != 0 & V[i] == 0 ):
            DFS(i)  # 인접하고 방문하지 않은 노드로 이동


# DFS 연습문제
# Input
# 5 6
# 1 2 1 3 3 2 2 5 3 4 5 4

def dfs(n, V):
    visited[n] = 1 # n번 노드에 방문 표시
    print(n, end=' ') # n번 노드에서 할 일
    for i in range(1,V+1): # 모든 노드 i에 대해
        if adj[n][i] == 1 and visited[i] == 0: # n에 인접하고, 방문하지 않았으면
            dfs(i, V) # i노드로 이동


# 인접행렬 생성
V, E = map(int, input().split())
adj = [[0]*(V+1) for _ in range(V+1)]
edge = list(map(int, input().split()))
visited = [0]*(V+1)
for i in range(E):
    n1 = edge[i*2]
    n2 = edge[i*2+1]
    adj[n1][n2] = 1
    # adj[n2][n1] = 1 # 방향성이 없는 무향그래프인 경우

for i in range(V+1):
    for j in range(V+1):
        if i != 0 and j != 0:
            print(adj[i][j], end=' ')
    print()

print()
dfs(1, V)


# 반복구조 dfs는 지나온 노드를 스택에 저장하거나, 방문하지 않고 남겨놓은 노드를 스택에 저장

def dfs2(n, V): # 반복구조의 dfs
    s = [] # 스택 생성
    used = [0]*(V+1) # 중복확인
    s.append(n) # push(n) 시작점 저장
    used[n] = 1
    while len(s) != 0: # 스택이 비어있지 않으면
        n = s.pop() # pop()
        print(n, end=' ')
        for i in range(1, V+1):
            if adj[n][i] ==1 and used[i] == 0: # i가 인접이고, 스택에 들어있지 않으면,
                s.append(i) # 인접 목록 추가
                used[i] = 1 # 목록에 추가 표시


# 인접행렬 생성
V, E = map(int, input().split())
adj = [[0]*(V+1) for _ in range(V+1)]
edge = list(map(int, input().split()))
visited = [0]*(V+1)
for i in range(E):
    n1 = edge[i*2]
    n2 = edge[i*2+1]
    adj[n1][n2] = 1
    # adj[n2][n1] = 1 # 방향성이 없는 무향그래프인 경우

dfs2(1, V)