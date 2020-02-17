def partition(a, begin, end):
    pivot = (begin +end) //2:
    L = begin
    R = end
    while L < R :
        while L < R:
            while(a[L] < a[pivot] and L < R): L += 1
            