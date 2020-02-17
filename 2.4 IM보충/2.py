# 구구단

# 첫번째 방법
n = int(input())
i = 0
while i<= 8:
    i += 1
    result = n * i
    print(f'{n} * {i} = {result}')

# 두번째 방법
dan = int(input())
i = 1
while i<= 9:
    print('{} * {} = {} '.format(dan, i, dan*i))
    i += 1

# for문
# 조건보다 횟수에 비중을 둘 때 사용하는 반복문
# 시작값, 종료값, 증감을 한문장에 쓴다.
# 조건이 참인 동안 실행

# 문제: 0부터 10까지의 합을 구하시오.

result = 0
for i in range(11):
    result += i
print(result)
print('1부터 10까지의 합 = {}'.format(result))

# 문제: 5부터 10까지의 합을 구하시오.

result = 0
for i in range(5,11):
    result += i
print(result)

# 문제: 1부터 10까지 중 짝수만 더하시오.

result = 0
for i in range(11):
    if i %2 == 0:
        result += i
print(result)

result = 0
for i in range(5,11,2):
    result += i
print(result)