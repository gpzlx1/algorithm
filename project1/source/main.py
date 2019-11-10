from countSort import countSort
from mergeSort import mergeSort
from heapSort import heapSort
from quickSort import quickSort

import time
import os
import sys

def check_array(array):
    length = len(array)
    for i in range(1, length-1):
        if array[i-1] > array[i]:
            return False    
    return True

def read_input(N):
    num = 2**N
    array = [0] * num
    with open("input/input_string.txt","r") as f:
        for i in range(num):
            array[i] = (int(f.readline()))
    return array

def sort_all(N): # num of array = 2**N
    input = read_input(N)  #读取待排序数据，input为python list
    ret = {}     #python 字典
    ret["origin"] = input   #初始数据
    
    #ret["merge_sort"][0] 存放排序结果 ret["merge_sort"][1] 存放排序所花时间，下同
    begin = time.time()
    ret["merge_sort"] = [ mergeSort(input.copy(), 0, len(input) - 1)  ]
    end = time.time()
    ret["merge_sort"].append(end - begin)

    begin = time.time()
    ret["heap_sort"]  = [   heapSort(input.copy())  ]
    end = time.time()
    ret["heap_sort"].append(end - begin)

    begin = time.time()
    ret["quick_sort"] = [   quickSort(input.copy(), 0, len(input) - 1)  ]
    end = time.time()
    ret["quick_sort"].append(end - begin)

    begin = time.time()
    ret["count_sort"] = [   countSort(input.copy(), 65536)  ]
    end = time.time()
    ret["count_sort"].append(end - begin)

    return ret

if __name__ == "__main__":
    N = int(sys.argv[1])
    if N > 15:
        print("usage: python main.py N")
        print("N should be smaller than 16")
        exit()
    ret = sort_all(N)
    for key, value in ret.items():
        if key == "origin":
            continue

        if not os.path.exists("output/" + key):
            os.makedirs("output/" + key)

        if check_array(value):
            print(key + ": no error")
            f = open("output/" + key + "/" + "result_" + str(N) + ".txt", "w")
            for i in range(2**N):
                f.writelines(str(value[0][i]) + "\n")
            f.close()
            f = open("output/" + key + "/" + "time.txt", "a+")
            f.writelines("time cost of N = {} : ".format(N))
            f.writelines(str(value[1]) + " ms\n")
            f.close()
        else:
            print(key + ": find errors")
    