class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        divisions = defaultdict(lambda: -1.0)
        variables = set()
        for idx, (var1, var2) in enumerate(equations):
            divisions[(var1, var2)] = values[idx]
            divisions[(var2, var1)] = 1 / values[idx]
            divisions[(var1, var1)] = 1
            divisions[(var2, var2)] = 1
            variables.add(var1)
            variables.add(var2)
        
        for var3 in list(variables):
            for var1 in list(variables):
                for var2 in list(variables):
                    if (var1, var3) in divisions and (var3, var2) in divisions:
                        divisions[(var1, var2)] = divisions[(var1, var3)] * divisions[(var3, var2)]
        
        return [divisions[(var1, var2)] for var1, var2 in queries]