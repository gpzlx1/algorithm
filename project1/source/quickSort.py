#array 待排序的数组
#beg 数组array开始的位置(included)
#end 数组array借宿的位置(included)
def partition(array, beg, end):
    if beg >= end:
        return beg
    key = array[beg]
    b = beg
    e = end
    while(b < e):
        while array[e] > key and b < e:
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



