class Solution:
    def __init__(self):
        self.unique1 = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
        self.unique2 = ['Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen']
        self.unique3 = ['Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']
        self.unique4 = ['Thousand', 'Million', 'Billion']

    def hundredize(self, num):
        num = '000' + num
        word = ''
        hundred, ten, one = int(num[-3]), int(num[-2]), int(num[-1])

        if hundred:
            word += self.unique1[hundred] + ' Hundred'
        if ten:
            if ten == 1:
                word += ' ' + self.unique2[one]
                return word.strip()
            
            word += ' ' + self.unique3[ten-2]
        if one:
            word += ' ' + self.unique1[one]
        
        return word.strip()

    def numberToWords(self, num: int) -> str:
        if num == 0:
            return self.unique1[num]
        
        str_num = str(num)
        list_num = [str_num[-10:-9], str_num[-9:-6], str_num[-6:-3], str_num[-3:]]
        word = ''
        
        for i in range(len(list_num)):
            section = self.hundredize(list_num[i])
            word += section
            if section and i < 3:
                word += ' ' + self.unique4[3-i-1] + ' '
        
        return word.strip()
