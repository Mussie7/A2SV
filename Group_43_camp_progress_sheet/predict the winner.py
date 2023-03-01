class Solution:
    def recurr(self, l, r, nums, turn):
        if l == r:
            if turn > 0:
                return nums[l], 0
            else:
                return 0, nums[l]
        
        if (turn, l, r) in self.memo:
            return self.memo[(turn, l, r)]
            
        lp1, lp2 = self.recurr(l+1, r, nums, -turn)
        rp1, rp2 = self.recurr(l, r-1, nums, -turn)
        
        if turn > 0:
            lp1 += nums[l]
            rp1 += nums[r]
        else:
            lp2 += nums[l]
            rp2 += nums[r]
        
        if (turn > 0 and lp1 > rp1) or (turn < 0 and lp2 > rp2):
            self.memo[(turn, l, r)] = lp1, lp2
            return lp1, lp2
        
        self.memo[(turn, l, r)] = rp1, rp2
        return self.memo[(turn, l, r)]


    def PredictTheWinner(self, nums: List[int]) -> bool:
        self.memo = {}
        player1, player2 = self.recurr(0, len(nums)-1, nums, 1)
        return player1 >= player2
