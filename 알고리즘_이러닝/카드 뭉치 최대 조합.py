def max_product(left_cards, right_cards):
    # 코드를 작성하세요.
    maxx = -1
    for i in range(len(left_cards)):
        for j in range(len(right_cards)):
            maxx = max(maxx, left_cards[i]*right_cards[j])

    return maxx
# 테스트
print(max_product([1, 6, 5], [4, 2, 3]))
print(max_product([1, -9, 3, 4], [2, 8, 3, 1]))
print(max_product([-1, -7, 3], [-4, 3, 6]))