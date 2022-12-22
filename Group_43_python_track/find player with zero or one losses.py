class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        players, losers = {}, set([])
        for match in matches:
            if match[0] not in players and match[0] not in losers:
                players[match[0]] = 0
            
            if match[1] in losers:
                continue
            elif match[1] in players and players[match[1]] == 1:
                losers.add(match[1])
                del players[match[1]]
            else:
                players[match[1]] = 1                
        
        winners, oneTimers = [], []
        for player in players:
            if not players[player]:
                winners.append(player)
            elif players[player] == 1:
                oneTimers.append(player)
        
        winners.sort()
        oneTimers.sort()
        return [winners, oneTimers]
