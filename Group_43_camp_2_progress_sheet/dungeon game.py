class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        m, n = len(dungeon), len(dungeon[0])
        dungeon.append([inf] * (n + 1))
        dungeon[-1][-2] = 1
        for i in range(m-1, -1, -1):
            dungeon[i].append(inf)
            for j in range(n - 1, -1, -1):
                dungeon[i][j] = max(1, min(dungeon[i+1][j], dungeon[i][j+1]) - dungeon[i][j])
        
        return dungeon[0][0]
