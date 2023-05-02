import threading
from sys import stdin,stdout,setrecursionlimit

setrecursionlimit(1 << 30)
threading.stack_size(1 << 27)

# import math
# import bisect
import collections

intInput = lambda : int(input())
tupInput = lambda : map(int, input().strip().split())
# intListInput = lambda : list(map(int, input().strip().split()))
# strListInput = lambda : input().strip().split()
# strInput = lambda : list(input().strip())

def run(n):
    def dfs(node):
        for neigh in graph[node]:
            if (color[neigh] == color[node]):
                return False
            elif not color[neigh]:
                color[neigh] = -color[node]
                if not dfs(neigh):
                    return False
            
        return True
        
    graph = collections.defaultdict(list)
    for _ in range(intInput()):
        node1, node2 = tupInput()
        graph[node1].append(node2)
        graph[node2].append(node1)
    
    color = [0] * (n + 1)
    color[1] = 1

    if dfs(1):
        print('BICOLOURABLE.')
    else:
        print('NOT BICOLOURABLE.')
    
    

def main():  
    while True:
        n = intInput()
        if not n:
            break
        run(n)


main_thread = threading.Thread(target=main)
main_thread.start()
main_thread.join()
