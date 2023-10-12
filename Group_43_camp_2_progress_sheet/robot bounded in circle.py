class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        # since the robot goes on the path infinitely we can't know for sure if it is stuck in a circle unless we simulate what would be an eternity
        instructions *= 4

        # 0 - left, 1 - right
        turn = {'north': ['west', 'east'], 'west': ['south', 'north'], 'south': ['east', 'west'], 'east': ['north', 'south']}
        dxn = {'north': (0, 1), 'south': (0, -1), 'west': (-1, 0), 'east': (1, 0)}

        curr_point = [0, 0]
        curr_dxn = 'north'
        for inst in instructions:
            if inst == 'G':
                curr_point[0] += dxn[curr_dxn][0]
                curr_point[1] += dxn[curr_dxn][1]
            elif inst == 'L':
                curr_dxn = turn[curr_dxn][0]
            else:
                curr_dxn = turn[curr_dxn][1]
        
        return curr_point == [0, 0]
