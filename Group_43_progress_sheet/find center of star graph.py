class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        counter = Counter()
        for node1, node2 in edges:
            counter[node1] += 1
            counter[node2] += 1
            if counter[node1] > 1:
                return node1
            if counter[node2] > 1:
                return node2
