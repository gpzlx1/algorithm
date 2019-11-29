import math as _math

class FibonacciHeapNode:
    
    def __init__(self, key = None, degree = None, p = None, child = None, \
                left = None, right = None, mark = None):
        self.key = key
        self.degree = degree
        self.p = p
        self.child = child
        self.left = left
        self.right = right
        self.mark = mark



class FibonacciHeap:

    def __init__(self):
        self.min = None
        self.cons = []
        self.keyNum = 0
        self.maxDegree = 0

    def makeHeap(self):
        heap = FibonacciHeap()
        heap.keNum = 0
        heap.min = 0
        heap.maxDegree = 0
        heap.cons = None
        return heap

    def makeNode(self, key):
        node = FibonacciHeapNode()
        node.key = key
        node.degree = 0
        node.left = node
        node.right = node
        node.p = None
        node.child = None
        return node

    #把节点插入到root之前
    def addNode(self, node : FibonacciHeapNode, root : FibonacciHeapNode):
        if node is None or root is None:
            return
        node.left = root.left
        root.left.right = node
        node.right = root
        root.left = node

    def removeNode(self, node : FibonacciHeapNode):
        node.left.right = node.right
        node.right.left = node.left


    def insert(self, node : FibonacciHeapNode):
        if self.keyNum == 0:
            self.min = node
        else:
            self.addNode(node, self.min)
            if node.key < self.min.key:
                self.min = node
        self.keyNum = self.keyNum + 1

    def insertKey(self,key):
        node = self.makeNode(key)
        self.insert(node)

    def makeCons(self):
        old = self.maxDegree
        self.maxDegree = int(_math.log2(self.keyNum) + 1)
        if old >= self.maxDegree:
            return
        self.cons = [None] * (self.maxDegree + 1)


    def removeMin(self):
        min = self.min
        if self.min == min.right:
            self.min = None
        else:
            self.removeNode(min)
            self.min = min.right
        min.right = min
        min.left = min.right
        return min

    def link(self, node : FibonacciHeapNode, root : FibonacciHeapNode):
        self.removeNode(node)
        if root.child == None:
            root.child = node
        else:
            self.addNode(node, root.child)
        node.p = root
        root.degree = root.degree + 1
        node.mark = False

    def consolidate(self):
        i = 0
        d = 0
        D = 0
        x = None
        y = None
        tmp = None
        self.makeCons()
        D = self.maxDegree + 1
        for i in range(D):
            self.cons[i] = None
        while self.min is not None:
            x = self.removeMin()
            d = x.degree
            while self.cons[d] is not None:
                y = self.cons[d]
                if x.key > y.key:
                    x, y = y, x
                self.link(y,x)
                self.cons[d] = None
                d += 1
            self.cons[d] = x
        self.min = None
        for i in range(D):
            if self.cons[i] is not None:
                if self.min is None:
                    self.min = self.cons[i]
                else:
                    self.addNode(self.cons[i], self.min)
                    if self.cons[i].key < self.min.key:
                        self.min = self.cons[i]


    def extractmin(self):
        if self is None or self.min is None:
            return None
        child = None
        min = self.min
        while min.child is not None:
            child = min.child
            self.removeNode(child)
            if child.right == child:
                min.child = None
            else:
                min.child = child.right
            self.addNode(child,self.min)
            child.p = None
        
        self.removeNode(min)
        if min.right == min:
            self.min = None
        else:
            self.min = min.right
            self.consolidate()
        self.keyNum = self.keyNum - 1
        return min


    def decreaseKey(self, node : FibonacciHeapNode, key):
        if self.min is None or node is None:
            return
        assert key <  node.key
        node.key = key
        parent = node.p
        if parent is not None and node.key < parent.key:
            self.cut(node, parent)
            self.cascadingCut(parent)
        if node.key < self.min.key:
            self.min = node


    def renewDegree(self, parent : FibonacciHeapNode, degree : int):
        if parent is None:
            return
        parent.degree = parent.degree - degree
        if parent.p is not None:
            self.renewDegree(parent.p, degree) 

    def cut(self, node : FibonacciHeapNode, parent : FibonacciHeapNode):
        if parent is None:
            return
        self.removeNode(node)
        self.renewDegree(parent, node.degree)
        if node == node.right:
            parent.child = None
        else:
            parent.child = node.right
        node.p = None
        node.left = node 
        node.right = node 
        node.mark = False 
        self.addNode(node, self.min)

    def cascadingCut(self, node : FibonacciHeapNode):
        if node is None:
            return
        parent = node.p
        if parent is not None:
            return
        if node.mark == False:
            node.mark = True
        else:
            self.cut(node, parent)
            self.cascadingCut(parent)

    def delete(self, node : FibonacciHeapNode):
        if self.min is None:
            return
        min = self.min
        self.decreaseKey(node, min.key - 1)
        self.extractmin()
        del node

    def search(self, key):
        if self.min is None:
            return None
        return self.searchFromRoot(self.min, key)

    def searchFromRoot(self, root : FibonacciHeapNode, key):
        t = root 
        p = None
        if root is None:
            return root
        while t != root.left:
            if t.key == key:
                p = t
                break
            else:
                p = self.searchFromRoot(t.child, key)
                if p is not None:
                    break
                t = t.right
        else:
            if t.key == key:
                p = t
            else:
                p = self.searchFromRoot(t.child, key)
        return p



        