class Solution:
    def populate(self, value, location, direction, road):
        i, j = location
        
        while 0 <= i < len(road) and 0 <= j < len(road[0]) and road[i][j] != '*':
            if value == 'T' and road[i][j] == 'S':
                return True
            if value == 'S' and road[i][j] == 'T':
                return True
            
            road[i][j] = value
            
            i += direction[0]
            j += direction[1]

    def strechOut(self, value, m, n, DIRECTION, road):
        for i in range(m):
            for j in range(n):
                if road[i][j] == value:
                    for dxn in DIRECTION:
                        if self.populate(road[i][j], (i+dxn[0], j+dxn[1]), dxn, road):
                            return True
                    return (i, j)
    
    def checkLastTurnRow(self, dxn, row, road):
        for j in range(len(road[0])):
            if road[row][j] == 'S':
                i = row + dxn
                while 0 <= i < len(road) and road[i][j] != '*':
                    if road[i][j] == 'T':
                        return True
                    i += dxn
    
    def checkLastTurnColumn(self, dxn, col, road):
        for i in range(len(road)):
            if road[i][col] == 'S':
                j = col + dxn
                while 0 <= j < len(road[0]) and road[i][j] != '*':
                    if road[i][j] == 'T':
                        return True
                    j += dxn
    
    def perfectPath(self):    
        m, n = (map(int, input().strip().split()))
        
        road = []
        for _ in range(m):
            road.append(list(input()))

        DIRECTION = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        
        start = self.strechOut('S', m, n, DIRECTION, road)
        target = self.strechOut('T', m, n, DIRECTION, road)
        
        if start == True: return True
        if target == True: return True
        
        dxn = 1 if target[0] - start[0] > 0 else -1
        if self.checkLastTurnRow(dxn, start[0], road): return True
        
        dxn = 1 if target[1] - start[1] > 0 else -1
        if self.checkLastTurnColumn(dxn, start[1], road): return True

s = Solution()

if s.perfectPath():
    print('YES')
else:
    print('NO')
