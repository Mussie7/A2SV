class Solution:
     def conquer(self, left, right):
        merged = []
        # create a prev variable for when the same element come in the right array you don't have to compute again
        prev = [-1, -1, -1]
        l = 0
        for r in range(len(right)):
            curr = self.ins[right[r]]
            # use the prev to check if the element has been computed for and not compute again
            if self.ins[right[r]] == prev[0]:
                self.min_max[right[r]][0] += prev[1]
                self.min_max[right[r]][1] += prev[2]
                merged.append(right[r])
                continue
            
            equal = False
            # merge and compute the count at the same time
            while l < len(left) and self.ins[left[l]] <= curr:
                # if the element found in left is equal to the current element in right the minimum has been counted
                if not equal and self.ins[left[l]] == curr:
                    self.min_max[right[r]][0] += l
                    prev[1] = l
                    equal = True
                
                # add the elements in left smaller than the current element in right to the merged array 
                merged.append(left[l])
                l += 1

            prev[0] = self.ins[right[r]]
            # don't forget to check if there is no element in left equal to the current element in right
            if not equal:
                self.min_max[right[r]][0] += l
                prev[1] = l

            # the remaining elements in left are the maximum count to the current element in right
            self.min_max[right[r]][1] += len(left) - l
            prev[2] = len(left) - l
            merged.append(right[r])

        # add the remaining elements in left to merged and return
        merged.extend(left[l:])
        return merged

    # the divide part of the divide and conquer algorithm
    def divide(self, arr):
        if len(arr) == 1:
            return arr
        
        n = len(arr)
        return self.conquer(self.divide(arr[:n//2]), self.divide(arr[n//2:]))

    def createSortedArray(self, instructions: List[int]) -> int:
        # make instructions global to access it
        self.ins = instructions
        # create a dictionary for holding the count of minimum and maximum numbers at the time of insertion of a particular number at an index
        self.min_max = {i: [0, 0] for i in range(len(instructions))}
        self.divide([i for i in range(len(instructions))])
        
        # calculate the insertion cost by taking the minimum out of the count computed in the divide and conquer
        insertion_cost = 0
        for ind in self.min_max:
            insertion_cost += min(self.min_max[ind])
        
        # modulo!
        return pow(insertion_cost, 1, 1000000007)
