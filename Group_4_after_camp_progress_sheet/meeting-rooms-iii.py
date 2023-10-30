class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        rooms = [i for i in range(n)]
        heap = []
        meeting_count = defaultdict(int)
        curr_time = 0
        for start, end in meetings:
            duration = end - start
            curr_time = max(start, curr_time)
            if not rooms:
                curr_time = max(curr_time, heap[0][0])
            
            while heap and heap[0][0] <= curr_time:
                heapq.heappush(rooms, heapq.heappop(heap)[1])
            
            curr_room = heapq.heappop(rooms)
            meeting_count[curr_room] += 1
            heapq.heappush(heap, (curr_time + duration, curr_room))
        
        most_meetings = 0
        target_room = 0
        for room in meeting_count:
            if meeting_count[room] > most_meetings:
                most_meetings = meeting_count[room]
                target_room = room
        return target_room