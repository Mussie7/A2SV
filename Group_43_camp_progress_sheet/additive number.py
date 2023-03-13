class Solution:
    def makeSequence(self, first, second, index):
        if index == len(self.num):
            return True
        
        third = ''
        for i in range(index, len(self.num)):
            if i == len(self.num) - 1 and (not first or not second):
                break

            third += self.num[i]

            if not first:
                if self.makeSequence(third, second, i+1):
                    return True
            elif not second:
                if self.makeSequence(first, third, i+1):
                    return True
            elif int(third) == int(first) + int(second):
                if self.makeSequence(second, third, i+1):
                    return True
            elif int(third) > int(first) + int(second):
                break
            
            if int(third) == 0:
                break
        
        return False

    def isAdditiveNumber(self, num: str) -> bool:
        self.num = num
        return self.makeSequence('', '', 0)
