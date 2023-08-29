class Solution:
    def find(self, node):
        if self.rep[node] == node:
            return node
        
        self.rep[node] = self.find(self.rep[node])
        return self.rep[node]
    
    def union(self, node1, node2):
        rep1, rep2 = self.find(node1), self.find(node2)
        if rep1 == rep2:
            return
        
        if self.rank[rep1] >= self.rank[rep2]:
            self.rep[rep2] = rep1
            self.rank[rep1] += self.rank[rep2]
            # when to segments union their segment sums are added together
            self.segment_sum[rep1] += self.segment_sum[rep2]
            # remove the already added segment
            del self.segment_sum[rep2]
        else:
            self.rep[rep1] = rep2
            self.rank[rep2] += self.rank[rep1]
            self.segment_sum[rep2] += self.segment_sum[rep1]
            del self.segment_sum[rep1]

    def maximumSegmentSum(self, nums: List[int], removeQueries: List[int]) -> List[int]:
        n = len(nums)
        self.rep = list(range(n))
        self.rank = [1] * n
        # make a segment sum dictionary assuming every index is its own segment
        self.segment_sum = {i:nums[i] for i in range(n)}
        
        # start from the end therefore simulate the array after the last removal
        for query in removeQueries:
            nums[query] = 0
        
        max_segment_sum = 0
        for i in range(n):
            # if two consecutive indices are not zero they belong to the same segment
            if i < n and nums[i] != 0 and num[i + 1] != 0:
                self.union(i, i+1)
            
            # get the segment sum for a non_zero index and compare with the max segment sum to for updation
            if nums[i] != 0:
                max_segment_sum = max(max_segement_sum, self.segment_sum[self.find(i)])
        
        query_sums = [max_segment_sum]
        # start constructing the previous segments by iterating backwards
        for i in range(len(removeQueries) - 1, 0, -1):
            query = removeQueries[i]
            # make sure to remove the zero from nums
            nums[query] = inf
            # once an index is restored union it if it connects to any other segments
            if query - 1 >= 0 and nums[query - 1] != 0:
                self.union(query, query - 1)
            if query + 1 < n and nums[query + 1] != 0:
                self.union(query, query + 1)
            
            # update the maximum segment sum
            max_segment_sum = max(max_segment_sum, self.segment_sum[self.find(query)])
            query_sums.append(max_segment_sum)
        
        return query_sums[::-1]
