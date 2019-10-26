import random
import sys

if len(sys.argv) != 3:
    print("usage: python3 createRandomArray.py N outPath")
    exit(-1)

index = sys.argv[1]
outPath = sys.argv[2]

with open(outPath + "/randomArray_" + index, "w") as f:
    index = int(index)
    for i in range(2**index):
        f.writelines(str(random.randint(1,65535)) + "\n")

