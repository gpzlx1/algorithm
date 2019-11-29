from MinHeap import operations
from FIBHeap import fib
import ReadData

if __name__ == '__main__':
    for index in range(1,6):
        print(index)
        BUILD = ReadData.read('input/data{}/build.txt'.format(index))
        DECREASE = ReadData.read('input/data{}/decrease.txt'.format(index))
        DELETE = ReadData.read('input/data{}/delete.txt'.format(index))
        EXTRACT = ReadData.read('input/data{}/extract.txt'.format(index))
        INSERT = ReadData.read('input/data{}/insert.txt'.format(index))

        print("build")
        heap = operations.BUILD_MIN_HEAP(BUILD[1:].copy())
        operations.CHECK(heap)

        Fheap = fib.FibonacciHeap()
        Fheap.makeHeap()
        for i in BUILD[1:]:
            Fheap.insertKey(i)

        print('insert')
        for x in INSERT[1:]:
            operations.INSERT(heap, x)
            operations.CHECK(heap)

        for i in INSERT[1:]:
            Fheap.insertKey(i)
                

        print('decrease')
        for i in DECREASE[1:]:
            x = heap.index(i)
            operations.DECREASE_KEY(heap, x, i-10)
            operations.CHECK(heap)
        
        for i in DECREASE[1:]:
            x = Fheap.search(i)
            Fheap.decreaseKey(x, x.key - 10)


        print('delete')
        for i in DELETE[1:]:
            x = heap.index(i)
            operations.DELETE(heap, x)
            operations.CHECK(heap)

        for i in DELETE[1:]:
            x = Fheap.search(i)
            Fheap.delete(x)

        print('extract')
        for i in range(EXTRACT[0]):
            min = operations.EXTRACT_MIN(heap)
            operations.CHECK(heap)

        for i in range(EXTRACT[0]):
            min = Fheap.extractmin()



    
    

