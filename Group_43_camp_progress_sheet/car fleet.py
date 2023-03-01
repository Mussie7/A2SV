class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        posSort = [i for i in range(len(position))]
        posSort.sort(key=lambda x: position[x])
        for i in range(len(posSort)):
            posSort[i] = (target - position[posSort[i]]) / speed[posSort[i]]
        
        decStack = []
        for time in posSort:
            while decStack and time >= decStack[-1]:
                decStack.pop()
            decStack.append(time)
        
        return len(decStack)
