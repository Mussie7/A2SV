# O(n) time and O(1)(not counting the sorting) space complexity

class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        '''
        1. sort both the trainers and the players
        2. since the trainers are the deciding factors(i.e. the trainer can't pick a player above its capacity), we start with the trainer with the lowest capacity and check in order
        3. at the same time we check for the players ability if it is greater we increment the trainer pointer and if it is less we increment both pointers after counting the pair
        '''

        trainers.sort()
        players.sort()

        pair = 0
        player_pointer = 0
        for trainer in trainers:
            if player_pointer == len(players):
                break
            
            if trainer >= players[player_pointer]:
                pair += 1
                player_pointer += 1
        
        return pair
