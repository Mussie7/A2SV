class ThroneInheritance:

    def __init__(self, kingName: str):
        self.lineage = defaultdict(list)
        self.dead = set()
        self.king = kingName

    def birth(self, parentName: str, childName: str) -> None:
        self.lineage[parentName].append(childName)

    def death(self, name: str) -> None:
        self.dead.add(name)

    def getInheritanceOrder(self) -> List[str]:
        def dfs(heir):
            if heir not in self.dead:
                succession.append(heir)
            
            for child in self.lineage[heir]:
                dfs(child)

        succession = []
        dfs(self.king)
        return succession

# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()
