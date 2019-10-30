# array 待排序的数组
# k 计数排序的范围 [0,k]
def countSort(array, k):
    length = len(array)
    c = [0] * (k + 1)   #我用python list存放数组，list在容量不足时，会自动申请更大的内存空间然后
    b = [0] * length    #整体拷贝过去，开销较大，所里这里通过`[0] * length`直接分配足够大的内存空间
    for j in array:
        c[j] = c[j] + 1
    
    for i in range(1, k+1):
        c[i] = c[i] + c[i-1]

    for j in range(length-1, -1, -1):
        b[c[array[j]] - 1] = array[j]
        c[array[j]] = c[array[j]] - 1

    return b

