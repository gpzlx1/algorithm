import random
import sys

if len(sys.argv) != 3:
    print("usage: python3 createRandomArray.py N outPath")
    exit(-1)

index = sys.argv[1]   # 读取N
outPath = sys.argv[2] # 读取输出文件夹

with open(outPath + "/input_string.txt", "w") as f:
    index = int(index)
    for i in range(2**index):
        f.writelines(str(random.randint(1,65535)) + "\n")

