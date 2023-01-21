class Solution:
    def flip(self, j, arr, i=0):
        while i < j:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1

    def pancakeSort(self, arr: List[int]) -> List[int]:
        n = len(arr)
        flip_index = []
        while n > 0:
            index = arr.index(n)

            if 0 < index < n-1:
                self.flip(index, arr)
                flip_index.append(index+1)
                self.flip(n-1, arr)
                flip_index.append(n)
            elif index == 0:
                flip_index.append(n)
                self.flip(n-1, arr)                

            n -= 1

        return flip_index
