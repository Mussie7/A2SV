class Solution:
    def validRequests(self, index, req):
        if index == len(self.requests):
            if list(self.in_and_out.values()).count(0) == len(self.in_and_out):
                self.maxReq = max(self.maxReq, req)
            return

        fro, to = self.requests[index]
        
        self.in_and_out[fro] -= 1
        self.in_and_out[to] += 1
        self.validRequests(index + 1, req + 1)

        self.in_and_out[fro] += 1
        self.in_and_out[to] -= 1
        self.validRequests(index + 1, req)

    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        self.requests = requests
        self.in_and_out = {i: 0 for i in range(n)}
        self.maxReq = 0
        self.validRequests(0, 0)
        
        return self.maxReq
