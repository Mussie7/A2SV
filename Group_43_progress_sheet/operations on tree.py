class LockingTree:

    def __init__(self, parent: List[int]):
        n = len(parent)
        self.graph = defaultdict(list)
        for i in range(n):
            if self.graph[parent[i]]:
                self.graph[parent[i]][0].append(i)
            else:
                self.graph[parent[i]].append([i])
            
            if not self.graph[i]:
                self.graph[i].append([])
            self.graph[i].append(parent[i])

        self.locked = [0] * (n + 1)

    def lock(self, num: int, user: int) -> bool:
        if not self.locked[num]:
            self.locked[num] = user
            return True
        return False

    def unlock(self, num: int, user: int) -> bool:
        if self.locked[num] and self.locked[num] == user:
            self.locked[num] = 0
            return True
        return False
    
    def upgrade(self, num: int, user: int) -> bool:
        def dfs1(node):
            lock_found = False
            for child in self.graph[node][0]:
                if self.locked[child]:
                    lock_found = True
                    self.locked[child] = 0
                if dfs1(child):
                    lock_found = True
            
            return lock_found
        
        def dfs2(node):
            if node == 0:
                return True
            if self.locked[self.graph[node][1]]:
                return False
            return dfs2(self.graph[node][1])

        if self.locked[num] or not dfs2(num) or not dfs1(num):
            return False

        self.locked[num] = user
        return True
        
        


# Your LockingTree object will be instantiated and called as such:
# obj = LockingTree(parent)
# param_1 = obj.lock(num,user)
# param_2 = obj.unlock(num,user)
# param_3 = obj.upgrade(num,user)
