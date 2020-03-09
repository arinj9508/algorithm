# n의 각 자릿수의 합을 리턴
def sum_digits(n):
    n = str(n)

    if len(n) < 2:
        return int(n)

    return sum_digits(n[:len(n) - 1]) + int(n[len(n) - 1])


# 테스트
print(sum_digits(22541))
print(sum_digits(92130))
print(sum_digits(12634))
print(sum_digits(704))
print(sum_digits(3755))