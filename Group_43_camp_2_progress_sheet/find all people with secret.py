class Solution:
    def find(self, node):
        if self.temp_rep[node] == node:
            return node
        self.temp_rep[node] = self.find(self.temp_rep[node])
        return self.temp_rep[node]
    
    def union(self, node1, node2):
        rep1, rep2 = self.find(node1), self.find(node2)
        if self.rep[rep1] == 0 or self.rep[rep2] == 0:
            self.rep[rep1] = self.rep[rep2] = self.rep[node1] = self.rep[node2] = 0
        
        self.temp_rep[rep2] = rep1

    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        self.rep = [i for i in range(n)]
        self.rep[firstPerson] = 0

        meeting_time = defaultdict(list)
        for p1, p2, time in meetings:
            meeting_time[time].append([p1, p2])

        for time in sorted(meeting_time.keys()):
            self.temp_rep = {}
            for p1, p2 in meeting_time[time]:
                if p1 not in self.temp_rep:
                    self.temp_rep[p1] = p1
                if p2 not in self.temp_rep:
                    self.temp_rep[p2] = p2

                self.union(p1, p2)
            
            for p1, p2 in meeting_time[time]:
                self.union(p1, p2)
        
        in_the_know = []
        for i in range(n):
            if self.rep[i] == 0:
                in_the_know.append(i)
        
        return in_the_know
