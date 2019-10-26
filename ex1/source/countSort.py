def countSort(array, k):
    length = len(array)
    c = [0] * (k + 1)
    b = [0] * length
    for j in array:
        c[j] = c[j] + 1
    
    for i in range(1, k+1):
        c[i] = c[i] + c[i-1]

    for j in range(length-1, -1, -1):
        b[c[array[j]] - 1] = array[j]
        c[array[j]] = c[array[j]] - 1

    return b

