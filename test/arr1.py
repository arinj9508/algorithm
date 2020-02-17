# arr1 = list()
# arr2 = []
# arr3 = [1, 2, 3]
# arr4 = [0]*10
#
# print(arr1)
# print(arr2)
# print(arr3)
# print(arr4)
# arr4[0] = 100
#
# arr3[2] = 10
# print(arr3)
#
# arr1.append(10)
# arr2.append(20)
# print(arr1)
# print(arr2)


# N <- size(arr) # 배열의 크기 N
# for i : 0 -> N-1 # 배열의 모든 원소 arr[i] 출력
#  print(arr[i])

# arr = [1,2,3,4,5,6]
# N = len(arr) # 배열의 크기 N
# 입력, 첫 줄에 정수의 개수 N, 다음 줄의 N개의 100이하의 자연수
# 입력 된 숫자 중 2의 배수가 몇 개인지 출력하는 프로그램을 작성하세요


# 6
# 1 2 3 4 5 6

# import sys
# sys.stdin = open('input.txt', 'r') # 외부에 텍스트 파일을 만들어 미리 인풋값을 지정

# N = int(input())
# # arr = list(map(int, input().split()))
# # count = 0
# #
# # for i in range(N): # 모든 원소 arr[i] 출력, i : 0 -> N-1
# #     if arr[i] % 2:
# #         count += 1
# #     else:
# #         count += 0
# # print(count)

test_case = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    print(arr)


# a = input().split()
#
# max = a[0]
# for i in range(len(a)):
#     if a[i] > max:
#         max = a[i]
#         print(i+1, max)