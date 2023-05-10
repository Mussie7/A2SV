# Topological sort using dfs
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def dfs(course):
            visited[course] = 1
            for req in graph[course]:
                if visited[req] == 2:
                    continue
                if visited[req] == 1 or not dfs(req):
                    return False
            
            visited[course] = 2
            return True

        graph = [[] for _ in range(numCourses)]
        for course, req in prerequisites:
            graph[course].append(req)
        visited = [0] * numCourses

        for course in range(numCourses):
            if visited[course] == 0 and not dfs(course):
                return False
        
        return True

    
# Topological sort using bfs
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        free = {i for i in range(numCourses)}
        graph = [[] for _ in range(numCourses)]
        req_counter = [0] * numCourses

        for course, req in prerequisites:
            graph[req].append(course)
            free.discard(course)
            req_counter[course] += 1
        
        que = deque(free)
        while que:
            course = que.popleft()
            for sequel in graph[course]:
                req_counter[sequel] -= 1
                if req_counter[sequel] == 0:
                    que.append(sequel)
                    free.add(sequel)
        
        return len(free) == numCourses
