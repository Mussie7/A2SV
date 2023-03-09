# template for doing backtracking questions

class Solution:
    def combinations(self, index, n, k):
        # check whether our base case which is our solution is valid
        if len(self.curr) == k:
            # documenting solution
            self.ans.append(self.curr.copy())
            return
        
        # iterate over the next candidates
        for i in range(index, n+1):
            # placing action
            self.curr.append(i)
            # calling the function recursively
            self.combinations(i+1, n, k)
            # removing action
            self.curr.pop()

    def combine(self, n: int, k: int) -> List[List[int]]:
        self.ans = []
        self.curr = []
        self.combinations(1, n, k)
        return self.ans
