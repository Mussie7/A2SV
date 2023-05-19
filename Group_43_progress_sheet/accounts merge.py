class Solution:
    def find(self, node):
        if self.rep[node] == node:
            return node
        # path compression
        self.rep[node] = self.find(self.rep[node])
        return self.rep[node]
    
    def union(self, node1, node2):
        rep1, rep2 = self.find(node1), self.find(node2)
        if rep1 == rep2:
            return
        # union by rank
        if self.rank[rep1] >= self.rank[rep2]:
            self.rep[rep2] = rep1
            self.rank[rep1] += self.rank[rep2]
        else:
            self.rep[rep1] = rep2
            self.rank[rep2] += self.rank[rep1]

    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        self.rep = [i for i in range(len(accounts))]
        self.rank = [1] * len(accounts)

        email_map = {}
        for i in range(len(accounts)):
            for email in accounts[i][1:]:
                if email in email_map:
                    self.union(i, email_map[email])
                else:
                    email_map[email] = i
        
        rep_map = defaultdict(set)
        for i in range(len(accounts)):
            rep = self.find(i)
            for email in accounts[i][1:]:
                rep_map[rep].add(email)
        
        return [[accounts[rep][0]] + sorted(rep_map[rep]) for rep in rep_map]
