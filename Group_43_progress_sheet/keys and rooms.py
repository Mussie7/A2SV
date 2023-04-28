class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        que = deque([0])
        visited = {0}
        while que:
            room = que.popleft()
            for key in rooms[room]:
                if key not in visited:
                    visited.add(key)
                    que.append(key)
        
        return len(visited) == len(rooms)
