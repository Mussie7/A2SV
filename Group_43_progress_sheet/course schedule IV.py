# topological sort bfs implementation
class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        in_degree = Counter()
        graph = defaultdict(list)
        for pre, course in prerequisites:
            graph[pre].append(course)
            in_degree[course] += 1
        
        que = deque()
        for course in range(numCourses):
            if in_degree[course] == 0:
                que.append(course)
        
        pre_map = [set() for i in range(numCourses)]
        while que:
            course = que.popleft()
            for advanced in graph[course]:
                in_degree[advanced] -= 1
                pre_map[advanced].add(course)
                pre_map[advanced] |= pre_map[course]

                if in_degree[advanced] == 0:
                    que.append(advanced)

        return [pre in pre_map[course] for pre, course in queries]
