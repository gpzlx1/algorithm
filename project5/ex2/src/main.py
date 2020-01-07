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
        raise ValueError('negative cycle')
    return D, P


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


from copy import deepcopy

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

N = [27, 81, 243, 729]
if __name__ == "__main__":
    for i in range(1, 5):
        for j in range(1, 3):
            path = "input/input" + str(i) + str(j) +".txt"
            G = readGraph(path, N[i-1])
            johnson(G)
