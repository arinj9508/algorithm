a = [64, 25, 10, 22, 11]

def selectionsort(a):
    for i in range(0, len(a)-1):
        minn = i
        for j in range(i+1, len(a)):
            if a[minn] > a[j]:
                minn = j
            a[minn], a[i] = a[i], a[minn]
        print(a)

selectionsort(a)



