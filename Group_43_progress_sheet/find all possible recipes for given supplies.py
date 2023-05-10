class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        graph = defaultdict(set)
        ing_count = Counter()
        for i, ingredient in enumerate(ingredients):
            for ing in ingredient:
                graph[ing].add(recipes[i])
        
            ing_count[recipes[i]] = len(ingredients[i])
        
        que = deque(supplies)
        cooked = []
        while que:
            done = que.popleft()
            for dependent in graph[done]:
                ing_count[dependent] -= 1

                if ing_count[dependent] == 0:
                    cooked.append(dependent)
                    que.append(dependent)
        
        return cooked
