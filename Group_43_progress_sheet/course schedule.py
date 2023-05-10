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
