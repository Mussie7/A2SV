class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        def overlap_count(left, up):
            nonlocal n
            overlap = 0
            for i in range(n):
                x = i + left
                if x >= n or x < 0:
                    continue

                for j in range(n):
                    y = j + up
                    if y >= n or y < 0:
                        continue

                    if img1[x][y] == img2[i][j] == 1:
                        overlap += 1
            
            return overlap

        @cache
        def dp(left, up):
            if abs(left) == n or abs(up) == n:
                return 0
            
            overlap = overlap_count(left, up)

            if left == 0:
                overlap = max(overlap, dp(left + 1, up), dp(left - 1, up))
            if up == 0:
                overlap = max(overlap, dp(left, up + 1), dp(left, up - 1))    

            if left > 0:
                if up > 0:
                    overlap = max(overlap, dp(left + 1, up), dp(left, up + 1))
                else:
                    overlap = max(overlap, dp(left + 1, up), dp(left, up - 1))
            else:
                if up > 0:
                    overlap = max(overlap, dp(left - 1, up), dp(left, up + 1))
                else:
                    overlap = max(overlap, dp(left - 1, up), dp(left, up - 1))

            return overlap

        
        n = len(img1)
        return dp(0, 0)
