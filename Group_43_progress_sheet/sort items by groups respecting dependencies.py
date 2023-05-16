class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        def dfs(item):
            # start by coloring the item gray
            visited[item] = 1
            for before in beforeItems[item]:
                # if the item that should come before the current element is in another group document it in the appearance graph
                if group[before] != group[item]:
                    appearance[group[item]].add(group[before])
                
                # check the color of the before-item
                if visited[before] == 2:
                    continue
                elif visited[before] == 1:
                    return False
                
                # if there is a loop backtrack
                if not dfs(before):
                    return False
            
            # at this point the item has reached its appropriate place in the group. color the item black
            visited[item] = 2
            items[group[item]].append(item)
            return True
        
        def dfs2(grp):
            # start by coloring the group gray
            visited[grp] = 1
            for before in list(appearance[grp]):
                # check the color of the before-group
                if visited[before] == 1:
                    return False
                elif visited[before] == 2:
                    continue
                
                # if there is a loop that means the order can't exist so backtrack
                if not dfs2(before):
                    return False
                
            # finally color the group black and extend it's elements into the sorted output
            visited[grp] = 2
            sorted_output.extend(items[grp])
            return True

        
        # first assign group for the items that doesn't have a group.
        # this is to differentiate between them when you sort them later.
        for i in range(n):
            if group[i] == -1:
                group[i] = m
                m += 1
        
        # create the actuall groups to put the elements in
        items = [[] for _ in range(m)]
        visited = [0] * n
        # create an appearance graph to map out how the groups should appear so that they keep their dependencies
        # basically create another graph to do a topological sort on
        appearance = defaultdict(set)
        for item in range(n):
            # do a topological sort by iterating over all the elements that exist
            if not visited[item] and not dfs(item):
                return []
        
        # now that the items are sorted in their respective groups, we need to sort the groups according to their dependencies
        visited = [0] * (m)
        sorted_output = []
        for grp in range(m):
            # do a topological sort by iterating over all the groups
            if not visited[grp] and not dfs2(grp):
                return []
              
        # the final result should be the sorted order the items should appear as respecting their dependencies
        return sorted_output
      
      
# p.s. the two dfs functions could be made into one since both basically do the same thing.
