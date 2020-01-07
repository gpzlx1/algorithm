#获取翻转所有边的图
def tr(G):
    #初始化翻转边的图GT
    GT=dict()
    for u in G.keys():
        GT[u]=GT.get(u,set())
    #翻转边
    for u in G.keys():
        for v in G[u]:
            GT[v].add(u)
    return GT

#获取按节点遍历完成时间递减排序的顺序
def topoSort(G):
    res=[]
    S=set()
    #dfs遍历图
    def dfs(G,u):
        if u in S:
            return
        S.add(u)
        for v in G[u]:
            if v in S:
                continue
            dfs(G,v)
        res.append(u)
    #检查是否有遗漏的节点
    for u in G.keys():
        dfs(G,u)
    #返回拓扑排序后的节点列表
    res.reverse()
    return res

#通过给定的起始节点，获取单个连通量
def walk(G,s,S=None):
    if S is None:
        s=set()
    Q=[]
    P=dict()
    Q.append(s)
    P[s]=None
    while Q:
        u=Q.pop()
        for v in G[u]:
            if v in P.keys() or v in S:
                continue
            Q.append(v)
            P[v]=P.get(v,u)
    #返回强连通图
    return P
    
G={
    'a':{'b','c'},
    'b':{'d','e','i'},
    'c':{'d'},
    'd':{'a','h'},
    'e':{'f'},
    'f':{'g'},
    'g':{'e','h'},
    'h':{'i'},
    'i':{'h'}
}

#记录强连通分量的节点
seen=set()
#储存强强连通分量
scc=[]
GT=tr(G)
print(GT)
for u in topoSort(G):
    if u in seen :
        continue
    C=walk(GT,u,seen)
    seen.update(C)
    scc.append(sorted(list(C.keys())))

print(scc)