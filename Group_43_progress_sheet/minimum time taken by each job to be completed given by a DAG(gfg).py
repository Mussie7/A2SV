from typing import List

import collections

class Solution:
    def minimumTime(self, n : int,m : int, edges : List[List[int]]) -> str:
        graph = collections.defaultdict(list)
        pre_count = [0] * (n + 1)
        for parent, child in edges:
            graph[parent].append(child)
            pre_count[child] += 1
        
        que = collections.deque([])
        for job in range(1, n + 1):
            if pre_count[job] == 0:
                que.append((job, 1))
        
        minimum_time = ['0'] * (n)
        while que:
            job, time = que.popleft()
            minimum_time[job-1] = str(time)
            for sequel in graph[job]:
                pre_count[sequel] -= 1
                if pre_count[sequel] == 0:
                    que.append((sequel, time + 1))
        
        return ' '.join(minimum_time)
