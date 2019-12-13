

[TOC]

# 算法基础 -- 上机实验4

## 实验内容及要求

###	实验内容

实现串匹配算法。其中，文本串T的长度为n，模式串P的长度为m，字符串中的字符均是随机生成的取自字符集[0-9A-Za-z]（共62个不同字符）的字符。(n, m)共有5组取值，分别为: (25，4), (28，8), (211,16), (214,32), (217,64)。具体字符串由助教给出。

算法：

* 朴素字符串匹配算法；
* Rabin-Karp算法；
* KMP算法； 
* Boyer-Moore-Horspool算法。

### 实验要求

实验格式：

* 实验需建立根文件夹，文件夹名称为：学号-project4，在根文件夹下需包括实验报告、和ex一个子文件夹，子文件夹又分别包含3个子文件夹：

  * input文件夹：存放输入数据
  * source文件夹：源程序
  * output文件夹：输出数据
* input:
* 生成的所有文本串和模式串存入一个文件。存入格式：T1 P1 T2 P2  …… T5 P5其中Ti表示文本串，Pi表示模式串，文本串和模式串交替出现，每组数据之间用换行符隔开。
  * 顺序读取文本串和模式串，进行匹配
* example：用KMP算法对长25 的文本串，长为4的模式串进行匹配时，其输入文件路径为：
  * 学号-project4/ex/input/input_strings.txt，顺序读取前2个字符串进行匹配。
* output:

  * 每个算法的运行结果存入一个文件，存入格式：文本串长度，模式串长度，首次成功匹配的起始位置（无成功匹配时输出-1），匹配所需运行时间（每组数据的输出单独为一行，各字段之间以空格分隔） 。
* 四个算法的结果存放路径：学号-project4/output/算法名/output.txt 
  

### 实验报告要求

1. 必须包含实验内容及要求、实验设备和环境、实验方法和步骤、实验结果与分析
2. 用适当的方法，或工具记录算法在执行时所消耗的时间；
3. 根据不同输入规模时记录的数据，画出算法在不同输入规模下的运行时间曲线图；比较你的曲线是否与课本中的算法渐进性能是否相同，若否，为什么，给出分析。

### 注意事项

* 实验报告中要有必要的实验过程截图和图表；
* 图片要有单位，横纵坐标等信息；
* ex1,ex2目录结构严格按照实验格式的要求；
* 代码中需要有必要的注释；
* 实验杜绝抄袭他人代码或者实验结果，如发现代码高度相似或者实验报告雷同者算0分；

## 实验设备和环境

* 实验设备：ThinkPad T470P
* 软件环境：
  * Host: windows 10 1903
  * client: windows subsystem for linux
  * wsl: Linux DESKTOP-3CEJIAK 4.4.0-18362-Microsoft #1-Microsoft
  * language: python 3.6.8

## 实验方法和步骤

### naive

朴素设计比较简单

```python
# T 为文本
# pattern 为模式
def naive(  T : str, pattern : str):
	n = len(T)
	m = len(pattern)
	for i in range(n-m+1):
		if pattern == T[i:i+m]:
			return i + 1
	return -1
```

### Rabin-Karp

Rabin-Karp实现主要有一个问题，python里`chr`类型并不是C中的char类型，不能直接与int进行转换，所以必须借助`ord()`函数，其功能为返回字符对应的Asicc

```python
# T 为文本
# pattern 为模式
# d 为基数
# q 为素数
def Rabin_Karp(T : str, pattern : str, d, q):
	n = len(T)
	m = len(pattern)
	h = pow(d,m-1)%q
	p = 0
	t = 0
	result = []
	for i in range(m): 				#计算初始p, t
		p = (d*p+ord(pattern[i]))%q
		t = (d*t+ord(T[i]))%q
	for s in range(n-m+1): 
		if p == t:					#可能匹配， 进行验证
			if pattern == T[s:s+m]:
				return s + 1
		
		if s < n-m:					#更新t
			t = ( t - h * ord(T[s]) ) % q
			t = (t*d + ord(T[s+m])) % q
			t = (t + q) % q
	return -1
```

### KMP

```python
# T 为文本
# pattern 为模式
def KMP(T : str, pattern : str):
	n = len(T)
	m = len(pattern)
	shift_array = compute_prefix_function(pattern) #得到状态转换表
	q = 0 
	for i in range(n):
		while q > 0 and pattern[q] != T[i]: #当前字符不匹配，右移
			q = shift_array[q]
		if pattern[q] == T[i]:				#当前字符匹配，不移动pattern，q++
			q = q + 1
		if q == m:							#存在字符匹配
			return i-m+1 + 1				
			q = shift_array[q-1]			#pattern右移一格
	return -1 

def compute_prefix_function(pattern : str):
	m = len(pattern)
	shift_array = []						#使用list存放状态转移目标
	shift_array.append(0)					#shift_array[0] = 0
	k = 0
	for q in range(1, m):
		while k > 0 and pattern[k] != pattern[q]:
			k = shift_array[k]
		if pattern[k] == pattern[q]:
			k = k + 1
		shift_array.append(k)
	return shift_array
```

### horspool

`horspool`算法的主要挑战书`bc`数组的计算，尤其时如何将字符映射为数字。为了解决这个问题，构造了`get_map`函数

```python
#get_map函数的功能为，统计T中字符集的大小，并为所有字符建立一个独一无二的映射，将字符转化为int
def get_map(T : str):
	map = {}
	i = 0
	for char in T:
		if char not in map.keys():	#该字符还没有被映射
			map[char] = i
			i = i + 1
	return map 
```

有了`get_map`函数，就可以比较简单实现`pre_bc`函数

```python
#pattern 为模式
#m 为map中的元素个数，即为字符集中字符的个数
#map即为get_map得到的map
def pre_bc(pattern : str, m : int, map : dict):
	n = len(pattern)
	bc = [ m ] * len(map)			#初始化

	for i in range(m-1):
		bc[map[pattern[i]]] = m - 1 - i

	return bc[0:len(map)]
```

有了`pre_bc`，`horspool`还有什么难的呢？

```python
def horspool(T : str, pattern : str, map : dict):
	n = len(T)
	m = len(pattern)
	bc = pre_bc(pattern, m, map)
	j = 0
	while j < n - m + 1:
		char = T[j + m - 1]
		if pattern[m-1] == char and pattern == T[j:j+m]: #找到匹配子串，返回
			return j + 1
		j += bc[map[char]]	#模式串右移
	return -1
```

二叉堆的数据结构采用python list形式实现

算法本质和书上并无太大差异，主要是为了适应python 从0开始的下标对`parent`, `left` ,`right` 做了一定改进

```python
def LEFT(i):
    return (i+1) * 2 - 1

def RIGHT(i):
    return (i+1) * 2 

def PARENT(i):
    return int((i+1)/2) - 1
```

其他的和书本上基本一致，所以主要介绍`DELETE`函数，此函数书上没有具体实现

```python
#此处的i为二叉堆中的元素,而不是元素所指向的关键字
def DELETE(A, i):
    length = len(A)
    if i >= length:
        print("There is no element {}".format(i))
        return -9999
    A[i] = A[-1]   #将最后一个元素填充到i处，并删除最后一个元素
    del A[-1]

    l = LEFT(i)
    r = RIGHT(i)
    length = length - 1
    #上诉操作完成后，有两种情况
    #第一种情况是，当前A[i] 比 它们的孩子都要大，此时比如不满足二叉堆性质，所以要用MIN_HEAPIFY函数将此节点下沉
    #第二种情况是，当时A[i]虽然比它的孩子小，但是A[i]的父亲比A[i]大，此时也不满足最小二叉堆性质，需要将A[i]和它的父亲交换
    #这两种情况下，最坏的情况下，时间复杂度也为O(logn)
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
```

### 斐波那契堆设计

斐波那契堆实现就比最小二叉堆复杂得多得多

我还是用python实现斐波那契堆

用两个对象来实现此斐波那契堆，一个为`FibonacciHeapNode`，另一个为`FibonacciHeap`

`FibonacciHeapNode`结构

```python	
class FibonacciHeapNode:
    def __init__(self, key = None, degree = None, p = None, child = None, \
                left = None, right = None, mark = None):
        self.key = key			#关键字
        self.degree = degree	#度
        self.p = p				#父亲节点
        self.child = child		#孩子节点
        self.left = left		#左兄弟节点
        self.right = right		#右兄弟节点
        self.mark = mark		#标记
```

`FibonacciHeap`结构

```python
class FibonacciHeap:
    def __init__(self):
        self.min = None		#最小元素的指针
        self.cons = []		#consolidate用到的数组
        self.keyNum = 0		#元素个数
        self.maxDegree = 0	#最大的度
```

`FibonacciHeap`有大量的方法，它们的介绍如下，具体细节不展开

```python
#初始化堆
makeHeap()
#建立带关键字的节点
makeNode(key)
#将node添加到root左侧
addNode(node : FibonacciHeapNode, root : FibonacciHeapNode)
#删除节点
removeNode(node : FibonacciHeapNode)
#插入节点
insert(node : FibonacciHeapNode)
#插入关键字（实际上先调用Makenode(key)， 随后addNode(node, heap.min)
insertKey(key)
#初始化heap.cons
makeCons()
#溢出heap.min
removeMin()
#书上说的那个功能
link(node : FibonacciHeapNode, root : FibonacciHeapNode)
#就是书上的说的那个功能，比较难形容
consolidate()
#移除heap.min, 并返回
extractmin()
#将某个节点的关键字减小到key
decreaseKey(node : FibonacciHeapNode, key)
#更新节点的degree
renewDegree(parent : FibonacciHeapNode, degree : int)
#书上说的那个功能
cut(node : FibonacciHeapNode, parent : FibonacciHeapNode)
#书上说的那个功能
cascadingCut(node : FibonacciHeapNode)
#删除节点
delete(node : FibonacciHeapNode)
#查找关键字key所对应的节点，是searchFromRoot的分装
search(key)
#在root这个堆中，查找关键key对应的节点
searchFromRoot(root : FibonacciHeapNode, key)
```

### 读取数据

专门设计了一个`readData`是读取输入数据

```python
def read(Path):
    with open(Path) as f:
        lines = f.readlines()
        ret = []
        for line in lines:
            ret.append(int(line))
    return ret
```

### Main函数设计

我这次实验Main函数设计的实在是有点丑，不是非常想放出来

就放一部分

```python
 		print("build")
        btime.writelines("build:    ")
        ftime.writelines("build:    ")
        t1 = time.time()
        heap = operations.BUILD_MIN_HEAP(BUILD[1:].copy())
        t2 = time.time()
        btime.writelines("{} \n".format(t2 - t1))
        
        ······
        ······
        
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

        btime.writelines("{} \n".format(sum))  #保存计时

        sum = 0
        for i in DELETE[1:]:
            x = Fheap.search(i)
            t1 = time.time()
            Fheap.delete(x)
            t2 = time.time()
            sum = sum + t2 - t1

        ftime.writelines("{} \n".format(sum)) #保存计时
```



## 实验结果与分析

### 正确性

四个算法对五种情况都返回了一样的结果，即为（下表从1开始）

1. 23
2. -1
3. 1436
4. -1
5. -1

和python自带的子串查找函数输出结果相一致，可以认为四种串匹配算法都正确。

### 时间复杂度分析



## 实验总结













































