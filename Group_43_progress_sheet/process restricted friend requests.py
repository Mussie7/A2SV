class Solution:
    def find(self, node):
        if self.rep[node] == node:
            return node
        self.rep[node] = self.find(self.rep[node])
        return self.rep[node]
    
    def union(self, node1, node2):
        rep1, rep2 = self.find(node1), self.find(node2)
        if rep1 == rep2:
            return

        if self.rank[rep1] >= self.rank[rep2]:
            self.rep[rep2] = rep1
            self.rank[rep1] += self.rank[rep2]
            self.unfriend[rep1].update(self.unfriend[rep2])
        else:
            self.rep[rep1] = rep2
            self.rank[rep2] += self.rank[rep1]
            self.unfriend[rep2].update(self.unfriend[rep1])

    def friendRequests(self, n: int, restrictions: List[List[int]], requests: List[List[int]]) -> List[bool]:
        self.unfriend = defaultdict(set)
        for friend, foe in restrictions:
            self.unfriend[friend].add(foe)
            self.unfriend[foe].add(friend)

        self.rep = list(range(n))
        self.rank = [1] * n
        approval = []
        for friend1, friend2 in requests:
            rep1, rep2 = self.find(friend1), self.find(friend2)
            approved = True
            # if one person in the list of people that can't be friends with the people in this group is friends with a person in the other group then these two people can't be friends
            for foe in list(self.unfriend[rep1]):
                if self.find(foe) == rep2:
                    approved = False
                    break

            for foe in list(self.unfriend[rep2]):
                if self.find(foe) == rep1:
                    approved = False
                    break

            approval.append(approved)
            if approved:
                self.union(friend1, friend2)
        
        return approval
