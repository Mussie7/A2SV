class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        que = collections.deque([i for i in range(len(tickets))])
        time = 1
        while que:
            i = que.popleft()
            tickets[i] -= 1
            if tickets[i] != 0:
                que.append(i)
            elif i == k:
                return time
            
            time += 1
        
        return time
