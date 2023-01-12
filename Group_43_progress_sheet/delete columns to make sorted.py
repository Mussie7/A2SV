class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        count = 0
        for column in zip(*strs):
            if column != tuple(sorted(column)):
                count += 1

        return count
