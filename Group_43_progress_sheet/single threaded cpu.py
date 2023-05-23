class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        for i in range(len(tasks)):
            tasks[i].append(i)
        tasks.sort(key=lambda x: x[0])

        heap, order = [], []
        index, time = 0, 1
        while index < len(tasks) or heap:
            if not heap:
                time = max(time, tasks[index][0])
            
            while index < len(tasks) and time >= tasks[index][0]:
                heapq.heappush(heap, [tasks[index][1], tasks[index][2]])
                index += 1
            
            duration, ind = heapq.heappop(heap)
            time += duration
            order.append(ind)
            
        return order
