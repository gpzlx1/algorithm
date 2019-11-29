from MinHeap import operations
from FIBHeap import fib
import ReadData
import time

if __name__ == '__main__':
    result = open("./output/binary_heap/result.txt", "w")
    fresult = open("./output/fibonacci_heap/result.txt", "w")
    btime = open("./output/binary_heap/time.txt", "w")
    ftime = open("./output/fibonacci_heap/time.txt", "w")
    for index in range(1,6):
        print(index)
        index_str = str(index * 100) + "\n"
        btime.writelines(index_str)
        ftime.writelines(index_str)
        fresult.writelines(index_str)
        result.writelines(index_str)

        BUILD = ReadData.read('input/data{}/build.txt'.format(index))
        DECREASE = ReadData.read('input/data{}/decrease.txt'.format(index))
        DELETE = ReadData.read('input/data{}/delete.txt'.format(index))
        EXTRACT = ReadData.read('input/data{}/extract.txt'.format(index))
        INSERT = ReadData.read('input/data{}/insert.txt'.format(index))

        print("build")
        btime.writelines("build:    ")
        ftime.writelines("build:    ")
        t1 = time.time()
        heap = operations.BUILD_MIN_HEAP(BUILD[1:].copy())
        t2 = time.time()
        btime.writelines("{} \n".format(t2 - t1))


        Fheap = fib.FibonacciHeap()
        Fheap.makeHeap()
        t1 = time.time()
        for i in BUILD[1:]:
            Fheap.insertKey(i)
        t2 = time.time()
        ftime.writelines("{} \n".format(t2 - t1))

        print('insert')
        ftime.writelines("insert:   ")
        btime.writelines("insert:   ")
        t1 = time.time()
        for x in INSERT[1:]:
            operations.INSERT(heap, x)
        t2 = time.time()
        btime.writelines("{} \n".format(t2 - t1))

        t1 = time.time()
        for i in INSERT[1:]:
            Fheap.insertKey(i)
        t2 = time.time()
        ftime.writelines("{} \n".format(t2 - t1))       
                

        print('decrease')
        ftime.writelines("decrease: ")
        btime.writelines("decrease: ")

        sum = 0
        for i in DECREASE[1:]:
            x = heap.index(i)

            t1 = time.time()
            operations.DECREASE_KEY(heap, x, i-10)
            t2 = time.time()
            sum = sum + t2 - t1

        btime.writelines("{} \n".format(sum))

        sum = 0
        for i in DECREASE[1:]:
            x = Fheap.search(i)

            t1 = time.time()
            Fheap.decreaseKey(x, x.key - 10)
            t2 = time.time()
            sum = sum + t2 - t1

        ftime.writelines("{} \n".format(sum))  


        print('delete')
        ftime.writelines("delete:   ")
        btime.writelines("delete:   ")
        


        sum = 0
        for i in DELETE[1:]:
            x = heap.index(i)

            t1 = time.time()
            operations.DELETE(heap, x)
            t2 = time.time()
            sum = sum + t2 - t1

        btime.writelines("{} \n".format(sum))

        sum = 0
        for i in DELETE[1:]:
            x = Fheap.search(i)

            t1 = time.time()
            Fheap.delete(x)
            t2 = time.time()
            sum = sum + t2 - t1
            
        ftime.writelines("{} \n".format(sum))  

        print('extract')
        ftime.writelines("extract:  ")
        btime.writelines("extract:  ")
        t1 = time.time()
        for i in range(EXTRACT[0]):
            min = operations.EXTRACT_MIN(heap)
            result.writelines(str(min) + ' ')
        t2 = time.time()
        btime.writelines("{} \n".format(t2 - t1))
        result.writelines('\n')

        t1 = time.time()
        for i in range(EXTRACT[0]):
            min = Fheap.extractmin()
            fresult.writelines(str(min.key) + ' ')
        t2 = time.time()
        ftime.writelines("{} \n".format(t2 - t1))  
        fresult.writelines('\n')



    
    

