
N, M = map(int,input().split())
a0 = [0]*(100+M)
arr2 = [[0]*50 + list(map(int,input().split())) + [0]*50 for _ in range(N)]
for i in range(50):
    arr2.insert(0, a0)
print(arr2)

