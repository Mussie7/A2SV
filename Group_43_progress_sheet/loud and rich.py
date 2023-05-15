# bfs(kahn's algorithm) topological sort implementation
class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        graph = defaultdict(list)
        que = {i for i in range(len(quiet))}
        above = defaultdict(int)
        for rich, poor in richer:
            graph[rich].append(poor)
            above[poor] += 1
            que.discard(poor)
        
        answer = [i for i in range(len(quiet))]
        que = deque(que)
        while que:
            rich = que.popleft()
            for poor in graph[rich]:
                answer[poor] = min(answer[poor], answer[rich], key=lambda i: quiet[i])
                
                above[poor] -= 1
                if above[poor] == 0:
                    que.append(poor)
        
        return answer
      
      
# dp looking dfs implementation
class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        @cache
        def dfs(person):
            for rich in graph[person]:
                answer[person] = min(answer[person], dfs(rich), key=lambda i: quiet[i])
            
            return answer[person]

        graph = defaultdict(list)
        for rich, poor in richer:
            graph[poor].append(rich)
        
        answer = [i for i in range(len(quiet))]
        for i in range(len(quiet)):
            answer[i] = dfs(i)
        
        return answer
