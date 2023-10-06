class Solution:
    # floyd warshall algorithm implementation
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        pre_map = defaultdict(set)
        for pre, course in prerequisites:
            pre_map[course].add(pre)
        
        for k in range(numCourses):
            for i in range(numCourses):
                for j in range(numCourses):
                    if i in pre_map[k] and k in pre_map[j]:
                        pre_map[j].add(i)
        
        query_output = []
        for pre, course in queries:
            query_output.append(pre in pre_map[course])
        
        return query_output
