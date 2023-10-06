class Solution:
    # floyd warshall algorithm implementation
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        division = {}
        variables = set()
        for i, (var1, var2) in enumerate(equations):
            division[(var1, var2)] = values[i]
            division[(var2, var1)] = 1 / values[i]
            
            division[(var1, var1)] = 1
            division[(var2, var2)] = 1
            
            variables.add(var1)
            variables.add(var2)
        
        variables = list(variables)
        for var1 in variables:
            for var2 in variables:
                for var3 in variables:
                    if (var2, var1) not in division or (var1, var3) not in division:
                        continue
                    
                    division[(var2, var3)] = division[(var2, var1)] * division[(var1, var3)]
                    division[(var3, var2)] = 1 / division[(var2, var3)]
        
        query_answers = []
        for var1, var2 in queries:
            if (var1, var2) not in division:
                query_answers.append(-1.0)
            else:
                query_answers.append(division[(var1, var2)])
        
        return query_answers
