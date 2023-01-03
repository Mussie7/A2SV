class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        DIRECTION = [(1, -1), (1, 0), (1, 1), (0, -1), (0, 1), (-1, -1), (-1, 0), (-1, 1)]
        queens = set([tuple(queen) for queen in queens])
        output = []

        for dxn in DIRECTION:
            coordinate = (king[0] + dxn[0], king[1] + dxn[1])
            
            while 0 <= coordinate[0] < 8 and 0 <= coordinate[1] < 8:
                if coordinate in queens:
                    output.append(coordinate)
                    break
                else:
                    coordinate = (coordinate[0] + dxn[0], coordinate[1] + dxn[1])
        
        return output
