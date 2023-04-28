class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        def find_iterations(combination, turns):
            for i in range(len(combination)):
                back = combination[:i] + str((int(combination[i])-1) % 10) + combination[i+1:]
                if back not in deadends and back not in visited:
                    visited.add(back)
                    que.append((back, turns + 1))

                forth = combination[:i] + str((int(combination[i])+1) % 10) + combination[i+1:]
                if forth not in deadends and forth not in visited:
                    visited.add(forth)
                    que.append((forth, turns + 1))

        deadends = set(deadends)
        que = deque([(target, 0)])
        visited = {target}
        while que:
            combo, turns = que.popleft()
            if combo == '0000':
                return turns

            find_iterations(combo, turns)
        
        return -1
