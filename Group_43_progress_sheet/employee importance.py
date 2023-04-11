"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def dfs(self, id):
        importance = self.id_map[id].importance
        for sub in self.id_map[id].subordinates:
            importance += self.dfs(sub)
        
        return importance

    def getImportance(self, employees: List['Employee'], id: int) -> int:
        self.id_map = {}
        for employee in employees:
            self.id_map[employee.id] = employee
        
        return self.dfs(id)
