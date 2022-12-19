class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        st = list(strs[0])
        for i in range(1, len(strs)):
            j = 0
            while j < len(st) and j < len(strs[i]) and st[j] == strs[i][j]:
                j += 1
            st = st[:j]

            if not st:
                return ''
        
        return "".join(st)
