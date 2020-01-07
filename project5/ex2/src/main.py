from copy import deepcopy
inf = float('inf')

def relax(W, u, v, D, P):
    d = D.get(u, inf) + W[u][v]
    if d < D.get(v, inf):
        D[v], P[v] = d, u
        return True
    return False

def bellman_ford(G, s):
    D, P = dict(), dict()
    D[0] = 0
    for rnd in G:
        changed = False
        for u in G:
            for v in G[u]:
                if relax(G, u, v, D, P):
                    changed = True
        if not changed:
            break
    else:
        return False, False
    return D, P

import random

def correctGraph(G):
    for u in G:
        for v in G[u]:
            if G[u][v] < 0:
                if random.randint(0,1) == 1:
                    G[u][v] = -G[u][v]
    return G
        
def testGraph(G):
    G = deepcopy(G)
    s = 0
    G[s] = {v: 0 for v in G}
    D, _ = bellman_ford(G, s)
    if type(D) != type(False):
        del G[s]
        return "Ok", G
    while type(D) == type(False):
        correctGraph(G)
        D, _ = bellman_ford(G, s)

    del G[s]
    return "Corrected", G
        

from heapq import heappush, heappop

def dijkstra(G, s):
    D, P, Q, S = {s: 0}, {}, [(0, s)], set()
    while Q:
        _, u = heappop(Q)
        if u in S:
            continue
        S.add(u)
        for v in G[u]:
            relax(G, u, v, D, P)
            heappush(Q, (D[v], v))
    return D, P




def johnson(G):
    G = deepcopy(G)
    s = 0
    G[s] = {v: 0 for v in G}
    h, _ = bellman_ford(G, s)
    del G[s]
    for u in G:
        for v in G[u]:
            G[u][v] += h[u] - h[v]
    D, P = dict(), dict()
    for u in G:
        D[u], P[u] = dijkstra(G, u)
        for v in G:
            if v not in D[u]:
                D[u][v] = inf
            else:
                D[u][v] += h[v] - h[u]
    return D, P   

def readGraph(path : str, n : int):
    Graph = {}
    with open(path, "r") as f:
        ctxs = f.readlines()
        for i in range(1, n + 1):
            Graph[i] = {}
        for ctx in ctxs:
            src, dst, weight = ctx.strip().split()
            src = int(src)
            dst = int(dst)
            weight = int(weight)
            Graph[src][dst] = weight
    return Graph

# u -> v
def get_path(P, u, v):
    if u == v:
        return "{} -> {}".format(u, v)
    if v not in P[u]:
        return None
    path = []
    path.append(str(v))
    k = P[u][v]
    while k != u:
        path.append(str(k))
        k = P[u][k]
    path.append(str(u))
    path.reverse()
    return " -> ".join(path)


import time 
N = [27, 81, 243, 729]
if __name__ == "__main__":
    out_time = "output/time.txt"
    f_time = open(out_time, "w")
    for i in range(1, 5):
        for j in range(1, 3):
            path = "input/input" + str(i) + str(j) +".txt"         
            G = readGraph(path, N[i-1])
            status, G = testGraph(G)
            print(status + " " + path)
            b = time.time()
            D, P = johnson(G)
            e = time.time()
            f_time.write("{} s\n".format(e-b))
            with open( "output/result" + str(i) + str(j) +".txt",  "w") as f:
                for u in D:
                    for v in sorted(D[u]):
                        if D[u][v] == inf:
                            f.write("{}->{}\t( None, inf )\n".format(u,v))
                        else:
                            f.write("{}->{}\t( ".format(u,v) + get_path(P, u, v) + ", {} )\n".format(D[u][v]))
