def is_palindrome(word):
    # 코드를 입력하세요.
    front = ''
    end = ''
    for i in range(len(word)//2):
        front += word[i]
        end += word[len(word)-1-i]

    if front == end:
        return True
    else:
        return False
# 테스트
print(is_palindrome("racecar"))
print(is_palindrome("stars"))
print(is_palindrome("토마토"))
print(is_palindrome("kayak"))
print(is_palindrome("hello"))