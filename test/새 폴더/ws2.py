import sys
sys.stdin = open('input2.txt', 'r')
#
#
# T = int(input())
# N = int(input())
# text = input()
# text_list = []
# num_list = []
#
#
# for i in text:
#     text_list.append(i)
#     num_list.append(int(i))
#
# count_num_list = [0]*len(num_list)
# for x in
#
# print('#{} {}'.format(T, num_list))
#
#
# A = [0,4,1,3,1,2,4,1]
# B = [0]*len(A)
# C = [0]*(max(A)+1)
#
# for x in A: # 카운트 배열 생성
#     C[x] += 1
#
# for i in range(1, len(C)): # 누적 합을 저장, 1부터 시작하는 것에 중의하자(1부터 해야 왼쪽이 존재)
#     C[i] += C[i-1] # 자신과 왼쪽까지 누적된 합을 더함
#
# print(C)
#
# for i in range(len(A)):
#     C[A[i]] -= 1
#     B[C[A[i]]] = A[i]
#
# print(C)
# print(B)


T = int(input())

for tc in range(1,T+1):
    N = int(input())
    num = list(map(int, input()))
    num_count = [0]*10
    M = 0
    for i in range(N):
        num_count[(num[i])] +=1
        max_idx = 0
        max_value = num_count[max_idx]
        for x in range(10):
            if max_value <= num_count[x]:
                max_value = num_count[x]
                max_idx = x
    print('#{} {} {}'.format(tc, max_idx, max_value))


        # x = 0
        #     M = 0
        #     if num_count[x]<num_count[x+1]:
        #         M = num_count[x+1]
        #     x += 1
        #     print(M)

    # print(num_count)
    # print('#{} {}'.format(tc,max(num_count)))