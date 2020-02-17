# 4 5 6 7 7 9 -> 떨어져서 입력될 때
# num = list(map(int, input().split()))

# 456779 연속적으로 입력될 때
num = list(input())
count = [0]*10

for x in num:
    count[int(x)] += 1
print(count)