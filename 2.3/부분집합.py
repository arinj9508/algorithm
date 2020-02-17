arr = [1,2,3]
bit = [0]*3
for i in range(2):
    bit[0] = i
    for j in range(2):
        bit[1] = j
        for k in range(2):
            bit[2] = k
            print(bit, end=' ')
            for n in range(3):
                if bit[n] ==1:
                    print(arr[n], end=' ')
            print()
