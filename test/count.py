A = [0, 4, 1, 3, 1, 2, 4, 1]
B = [0]*len(A)
C = [0]*(max(A)+1)

for x in A: # 카운트배열 생성
    C[x] += 1

for i in range(1, len(C)): # 누적 합을 저장
    C[i] += C[i-1] # 자신과 왼쪽까지 누적된 합을 더함


for i in range(len(A)):
    C[A[i]] -= 1
    B[C[A[i]]] = A[i]
print(B)