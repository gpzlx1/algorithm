

def genMaxHeap(array, length):
    mid = int(length / 2)
    a = list(range(1, mid + 1))
    a.reverse()
    for index in a:
        MAX_HEAPIFY(array, index, length)


def MAX_HEAPIFY(array, parent, length):
    left = parent * 2
    right = parent * 2 + 1
    if left <= length and array[parent - 1] < array[left - 1]:
        largest = left
    else:
        largest = parent

    if right <= length and array[largest-1] < array[right -1]:
        largest = right
    
    if largest != parent:
        array[parent - 1], array[largest - 1] = array[largest - 1], array[parent - 1]
        MAX_HEAPIFY(array, largest, length)
 
        
def heapSort(array):
    length = len(array)
    genMaxHeap(array, length)
    for i in range(length):
        length = length - 1
        array[length] ,array[0] = array[0], array[length]
        MAX_HEAPIFY(array, 1, length)

        

if __name__ == "__main__":
    a = [12, 13, 12,21 ,12,7,4 ,2, 3]
    heapSort(a)
    print(a)