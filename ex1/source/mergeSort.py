import sys
#reange inlcude ben end
def merge(array, ben, mid, end):
    if ben >= end:
        return
    L = array[ben:mid+1]
    R = array[mid+1:end+1]
    L.append(65536)
    R.append(65536)
    i = 0
    j = 0
    for k in range(ben, end+1):
        if L[i] <= R[j]:
            array[k] = L[i]
            i = i + 1
        else:
            array[k] = R[j]
            j = j + 1
    return array

def mergeSort(array, beg, end):
    if beg < end:
        mid = int((beg+end) / 2)
        mergeSort(array, beg, mid)
        mergeSort(array, mid+1, end)
        merge(array, beg, mid, end)
        
    return array

