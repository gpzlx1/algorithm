def LEFT(i):
    return (i+1) * 2 - 1

def RIGHT(i):
    return (i+1) * 2 

def PARENT(i):
    return int((i+1)/2) - 1

def MIN_HEAPIFY(A, i):
    length = len(A)
    l = LEFT(i)
    r = RIGHT(i)
    if l < length and A[l] < A[i]:
        smallest = l
    else:
        smallest = i
    
    if r < length and A[r] < A[smallest]:
        smallest = r

    if smallest != i:
        A[i], A[smallest] = A[smallest], A[i]
        MIN_HEAPIFY(A, smallest)

def BUILD_MIN_HEAP(A):
    length = len(A)
    for i in range(int(length/2) - 1, -1, -1):
        MIN_HEAPIFY(A, i)
    return A

def EXTRACT_MIN(A):
    length = len(A)
    if length < 1:
        print("heap underflow")
        return -99999
    
    minValue = A[0]
    A[0] = A[-1]
    del A[-1]
    MIN_HEAPIFY(A, 0)
    return minValue

def DECREASE_KEY(A, i, k):
    if k > A[i]:
        print("new key is larger than current key")
        return -99999
    A[i] = k
    while i > 0 and A[PARENT(i)] > A[i]:
        A[i], A[PARENT(i)] = A[PARENT(i)], A[i]
        i = PARENT(i)
    return 0
    
def INSERT(A, k):
    A.append(k)
    DECREASE_KEY(A, len(A) - 1, k)

#此处的i为二叉堆中的元素,而不是元素所指向的关键字
def DELETE(A, i):
    length = len(A)
    if i >= length:
        print("There is no element {}".format(i))
        return -9999
    A[i] = A[-1]        #将最后一个元素填充到i处，并删除最后一个元素
    del A[-1]

    l = LEFT(i)
    r = RIGHT(i)
    length = length - 1
    #上诉操作完成后，有两种情况
    #第一种情况是，当前A[i] 比 它们的孩子都要大，
    #此时比如不满足二叉堆性质，所以要用MIN_HEAPIFY函数将此节点下沉
    #第二种情况是，当时A[i]虽然比它的孩子小，但是A[i]的父亲比A[i]大，
    #此时也不满足最小二叉堆性质，需要将A[i]和它的父亲交换
    if (l < length and A[i] > A[l]) or  (r < length and A[i] > A[r]):
        MIN_HEAPIFY(A, i)
    else:
        p = PARENT(i)
        x =  i
        while p >= 0 and A[p] > A[x]:
            A[p], A[x] = A[x], A[p]
            x = p
            p = PARENT(x)
    return 0

def CHECK(A):
    length = len(A)
    for i in range(length):
        l = LEFT(i)
        r = RIGHT(i)
        if l < length and A[i] > A[l]:
            print("error: {}, {} is larger then {} {}".format(i, A[i], l, A[l]))
        if r < length and A[i] > A[r]:
            print("error: {}, {} is larger then {} {}".format(i, A[i], r, A[r]))

 