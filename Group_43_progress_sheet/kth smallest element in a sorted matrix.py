class Solution:
    # heap implementation
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        if k == n * n:
            return matrix[-1][-1]
            
        heap = [(matrix[0][0], 0, 0)]
        visited = {(0, 0)}
        while k:
            curr_element, i, j = heapq.heappop(heap)
            k -= 1
            if k == 0:
                return curr_element

            if i < n - 1 and (i+1, j) not in visited:
                heapq.heappush(heap, (matrix[i+1][j], i+1, j))
                visited.add((i+1, j))
            
            if j < n - 1 and (i, j+1) not in visited:
                heapq.heappush(heap, (matrix[i][j+1], i, j+1))
                visited.add((i, j+1))


# an actually better heap solution(time wise) according to leetcode
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        if k == n * n:
            return matrix[-1][-1]
            
        heap = [(matrix[0][0], 0, 0)]
        visited = {(0, 0)}
        while k:
            curr_element, i, j = heapq.heappop(heap)
            k -= 1
            if k == 0:
                return curr_element

            if i < n - 1 and (i+1, j) not in visited:
                heapq.heappush(heap, (matrix[i+1][j], i+1, j))
                visited.add((i+1, j))
            
            if j < n - 1 and (i, j+1) not in visited:
                heapq.heappush(heap, (matrix[i][j+1], i, j+1))
                visited.add((i, j+1))
