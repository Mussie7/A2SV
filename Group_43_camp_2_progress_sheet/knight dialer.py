class Solution:
    def knightDialer(self, n: int) -> int:
        @cache
        def dp(cell, n):
            if n == 0:
                return 1

            numbers = 0
            for jump in graph[cell]:
                numbers += dp(jump, n - 1)
            
            return pow(numbers, 1, 10**9 + 7)
        
        graph = {0: [4, 6], 1: [6, 8], 2: [7, 9], 3: [4, 8], 4: [0, 3, 9], 5: [], 6: [0, 1, 7], 7: [2, 6], 8: [1, 3], 9: [2, 4]}
        numbers_count = 0
        for cell in range(10):
            numbers_count += dp(cell, n - 1)

        return pow(numbers_count, 1, 10**9 + 7)
