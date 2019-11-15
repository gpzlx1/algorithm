import numpy as np
import time 
#the root path should be ex1
inputFile = 'input/input.txt'

def readData(Path):
    ret = {}
    with open(Path, 'r') as f:
        while(True):
            N = f.readline()
            if(len(N) == 0):
                break
            Key = f.readline()
            PKey = f.readline()
            Key = [float(i) for i in Key.split()]
            PKey = [float(i) for i in PKey.split()]
            ret[int(N)] = [Key, PKey]
    return ret
#p 为关键字搜索概率
#q 为伪关键字搜索概率
#n 为规模
def optimal_bst(p,q,n):
    e = np.zeros((n+2, n+1))
    w = np.zeros((n+2,n+1))
    root = np.zeros((n+1,n+1))
    for i in range(1, n+2):
        e[i][i-1] = q[i-1]
        w[i][i-1] = q[i-1]
    for l in range(1,n+1):
        for i in range(1, n-l+2):
            j = i+l-1
            e[i][j] = 99999
            w[i][j] = w[i][j-1] + p[j-1] + q[j]
            for r in range(i, j+1):
                t = e[i][r-1] + e[r+1][j] + w[i][j]
                if t < e[i][j]:
                    e[i][j] = t
                    root[i][j] = r

    return e, root

#根据optimal_bst产生的root矩阵输出先序遍历的树结构
#table为 root 矩阵
#begin 为开始的关键字下标
#end 为结束的关键字下表
#i 为伪关键字的序号

def print_tree(table,begin,end, i):
    root = int(table[begin][end])       #根据root表的性质，root[begin][end]即为关键字表从begin到end所对应的最优二叉搜索树的根节点
    print('k{}'.format(root),end=' ')   #先序遍历输出根节点
    if root == begin:                   #此时，此root节点没有关键字左子树，只有伪关键字左子树
        print('d{}'.format(i),end=' ')  #输出此伪关键字节点
        i = i + 1                       #i++, 指向下一个伪关键字节点
    else:                               #还有关键字左子树，递归查询
        i = print_tree(table, begin, root-1, i) 
    
    if root == end:                     #对右子树分析，同理
        print('d{}'.format(i),end=' ')
        i = i + 1
    else:
        i = print_tree(table, root+1, end, i)
    return i
    
    
    


if __name__ == '__main__':
    timeTXT = open('output/time.txt','w')
    ret = readData(inputFile)
    for key, value in ret.items():
        p, q = value
        t1 = time.time()
        e, root = optimal_bst(p, q, key)
        t2 = time.time()
        timeTXT.writelines(str(t2-t1) + ' ms\n')
        print(e[1][-1], end=', ')
        print_tree(root, 1, key, 0)
        print()
    timeTXT.close()