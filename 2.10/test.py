# '''
# a = 'abc'
# print(a[1])
# a[1] = 'd'
# # 문자열은 tuple과 같이 요소를 변경할 수 없다.
# #'str' object does not support item assignment
# print(a[1])
# '''
#
# a = 'abc'
# b = 'abc'
# c = 'abe'
# print(a==b)
# print(a==c)
# print(c=='abe')


number = {'ZRO': 0, 'ONE': 1, 'TWO': 2, 'THR': 3, 'FOR': 4, 'FIV': 5, 'SIX': 6, 'SVN': 7, 'EGT': 8, 'NIN': 9}
keys = number.keys()
for i in keys:
    print(i)