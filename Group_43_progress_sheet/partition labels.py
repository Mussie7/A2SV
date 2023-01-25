# time complexity - O(n)
# space complexity - O(1)
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        start = 0
        visited = set()
        partition = []
        
        while start < len(s):
            end = s.rindex(s[start])
            visited.add(s[start])
            
            while start <= end:
                if s[start] not in visited:
                    end = max(end, s.rindex(s[start]))
                    visited.add(s[start])
                
                start += 1
            if partition:
                partition.append(start - cur)
                cur = start 
            else:
                partition.append(start)
                cur = start
        
        return partition
