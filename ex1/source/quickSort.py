#range include beg and end
def partition(array, beg, end):
    if beg >= end:
        return beg
    key = array[beg]
    b = beg
    e = end
    while(b < e):
        while array[e] > key:
            e = e - 1

        if b < e:
            array[b] = array[e]
            b = b + 1
        else:
            break

        while array[b] < key and b < e:
            b = b + 1
        
        if b < e:
            array[e] = array[b]
            e = e - 1
        else:
            break
        
    array[e] = key
    return e
    
def quickSort(array, beg, end):
    if beg >= end:
        return 
    mid = partition(array, beg, end)
    quickSort(array, beg, mid - 1)
    quickSort(array, mid + 1, end)
    return array

if __name__ == "__main__":
    a = [100, 3, 4, 3, 2, 6, 10]
    a = quickSort(a, 0, len(a) - 1)
    print(a)
