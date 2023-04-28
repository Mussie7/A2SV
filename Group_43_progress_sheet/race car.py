class Solution:
    def racecar(self, target: int) -> int:
        reverse = lambda speed : -1 if speed > 0 else 1
        
        que = deque([(0, 1, 0)])
        visited = {(0, 1)}
        while que:
            pos, speed, seq = que.popleft()
            if pos == target:
                return seq
            
            ac_pos = pos + speed
            ac_speed = speed * 2
            
            if ac_pos < 0 or (ac_pos, ac_speed) in visited:
                continue

            que.append((ac_pos, ac_speed, seq + 1))
            visited.add((ac_pos, ac_speed))
            
            rev_speed = -1 if speed > 0 else 1
            if (pos, rev_speed) in visited:
                continue

            que.append((pos, rev_speed, seq + 1))
            visited.add((pos, rev_speed))
