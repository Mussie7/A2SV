# bfs topological sort
class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for num1, num2 in adjacentPairs:
            graph[num1].append(num2)
            graph[num2].append(num1)

        for num in graph:
            if len(graph[num]) == 1:
                start = num
                break
        
        prev = -inf
        nums = []
        for _ in range(len(adjacentPairs) + 1):
            nums.append(start)
            for adj in graph[start]:
                if adj != prev:
                    prev, start = start, adj
                    break

        return nums
      
      
      
# dfs topological sort
class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        def is_edge(num):
            if num in edge_nums:
                edge_nums.remove(num)
            else:
                edge_nums.add(num)

        def dfs(num, parent=None):
            nums.append(num)
            for nxt in graph[num]:
                if nxt != parent:
                    dfs(nxt, num)

        edge_nums = set()
        graph = defaultdict(list)
        for num1, num2 in adjacentPairs:
            graph[num1].append(num2)
            graph[num2].append(num1)

            is_edge(num1)
            is_edge(num2)
        
        nums = []
        dfs(edge_nums.pop())
        return nums
