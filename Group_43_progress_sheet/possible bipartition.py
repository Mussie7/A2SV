class Solution:
    def dfs(self, person):
        for hater in self.haters[person]:
            if self.visited[hater]:
                if self.visited[hater] == self.visited[person]:
                    return True
                continue
            
            self.visited[hater] = -self.visited[person]
            
            if self.dfs(hater):
                return True

    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        self.haters = defaultdict(list)
        for hated, hater in dislikes:
            self.haters[hated].append(hater)
            self.haters[hater].append(hated)
        
        self.visited = [0] * (n+1)
        for i in range(1, n+1):
            if not self.visited[i]:
                self.visited[i] = 1
                if self.dfs(i):
                    return False

        return True
