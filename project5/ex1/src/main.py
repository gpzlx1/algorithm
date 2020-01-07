import math
N = [9, 27, 81, 243, 729]
readCount = [i for i in range(1,6)]
rootPath = "input"

def readGraph(path : str, n : int):
    Graph = {}
    with open(path, "r") as f:
        ctxs = f.readlines()
        for i in range(1, n + 1):
            Graph[i] = set()
        for ctx in ctxs:
            src, dst = ctx.strip().split()
            src = int(src)
            dst = int(dst)
            Graph[src].add(dst)
    return Graph

def tr(G):
    GT = dict()
    for value in G.keys():
        GT[value] = set()
    for key in G.keys():
        for value in G[key]:
            if value not in GT.keys():
                GT[value] = set()
            GT[value].add(key)
    
    return GT
    

def topoSort(G):
    res=[]
    S=set()

    def dfs(G,u):
        if u in S:
            return
        S.add(u)
        for v in G[u]:
            if v in S:
                continue
            dfs(G,v)
        res.append(u)

    for u in G.keys():
        dfs(G,u)

    res.reverse()
    return res

#通过给定的起始节点，获取单个连通量
def walk(G,s, S):
    Q=[]
    P=dict()
    Q.append(s)
    P[s]=None
    while Q:
        u = Q.pop()
        for v in G[u]:
            if v in P.keys() or v in S:
                continue
            Q.append(v)
            P[v]=P.get(v,u)

    return P

def getStrConnect(G):
    seen = set()
    scc = []
    GT = tr(G)
    for node in topoSort(G):
        if node in seen:
            continue
        C = walk(GT, node, seen)
        seen.update(C)
        scc.append(sorted(list(C.keys())))

    return scc

import time
if __name__ == "__main__":

    out = "output/" 
    with open(out + "time.txt", "w" ) as f:
        pass

    for i in range(5):
        path = rootPath + "/input" + str(i+1) +".txt"
        b = time.time()
        G = readGraph(path, N[i])
        e = time.time()
        ret = getStrConnect(G)
        
        with open(out + "time.txt", "a" ) as f:
            f.write(str(e-b) + " s \n")

        with open(out + "result" + str(i+1) +".txt", "w") as f:
            ret = sorted(ret)
            for i in ret:
                result = str(i)
                result = result.replace('[', '( ').replace(']', ' )')
                f.write(result)
        
        
