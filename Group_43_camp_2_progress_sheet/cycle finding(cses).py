import math
# import bisect
import collections
import heapq

intInput = lambda : int(input())
tupInput = lambda : map(int, input().strip().split())
intListInput = lambda : list(map(int, input().strip().split()))
strListInput = lambda : input().strip().split()
strInput = lambda : list(input().strip())

def run():
    n, m = tupInput()
    edges = []
    for _ in range(m):
        u, v, w = tupInput()
        edges.append([u, v, w])

    # n-1 iterations according to bellman ford's algorithm
    dist = [math.inf] * (n + 1)
    parent = [-1] * (n + 1)
    for _ in range(n-1):
        for u, v, w in edges:
            if dist[u] == math.inf:
                dist[u] = 0
                
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                parent[v] = u

    # checking for a cycle against the nth iteration
    cycle = -1
    for u, v, w in edges:
        if dist[u] == math.inf:
                dist[u] = 0
                
        if dist[u] + w < dist[v]:
            parent[v] = u
            cycle = v
            break

    # if a node in cycle is found find the cycle else indicate no cycle
    if cycle == -1:
        print('NO')
        return
    
    negative_cycle = []
    negative_cycle_map = {}
    while True:
        negative_cycle.append(cycle)
        if cycle in negative_cycle_map:
            print('YES')
            print(*reversed(negative_cycle[negative_cycle_map[cycle]:]))
            return
        negative_cycle_map[cycle] = len(negative_cycle) - 1
        cycle = parent[cycle]
    
        
testcases = 1
# testcases = intInput()
for _ in range(testcases):
    run()
    # print()
