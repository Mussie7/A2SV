class Solution:
    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
        def checkHappiness(x, y):
            idx = 0
            # for the preferences of x that come before y check if they prefer x more than their own pair
            while idx < n -1 and preferences[x][idx] != y:
                u = preferences[x][idx]
                v = pair_map[u]
                if pref[u][x] < pref[u][v]:
                    # if u prefers x more than v
                    # they are both unhappy!
                    unhappy.add(x)
                    unhappy.add(u)
                    break
                
                idx += 1

        n = len(preferences)
        pref = [[-1] * n for _ in range(n)]
        # assign the preferences index for an easy comparison
        for i in range(n):
            for j, friend in enumerate(preferences[i]):
                pref[i][friend] = j

        # for easy access create a pair map
        pair_map = {}
        for u, v in pairs:
            pair_map[u] = v
            pair_map[v] = u

        unhappy = set()
        for x, y in pairs:
            if x not in unhappy:
                checkHappiness(x, y)
            if y not in unhappy:
                checkHappiness(y, x)
        
        return len(unhappy)
