class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        friends = [i+1 for i in range(n)]
        index = 0

        while len(friends) > 1:
            index += k - 1
            index %= len(friends)
            friends.pop(index)
            index %= len(friends)
        
        return friends[0]
