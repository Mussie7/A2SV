class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        output, block = [], False
        for line in source:
            cur_line = ''
            not_append = False
            i = 0
            if block:
                block_end = line.find('*/')
                if block_end != -1:
                    i = block_end + 2
                    block = False
                    not_append = True
                else:
                    continue
            
            while i < len(line):
                if line[i] == '/' and i < len(line) - 1 and line[i+1] == '/':
                    break
                if line[i] == '/' and i < len(line) - 1 and line[i+1] == '*':
                    block = True
                    block_end = line[i+2:].find('*/')
                    if block_end != -1:
                        i += block_end + 2 + 2
                        block = False
                        continue
                    else:
                        break

                cur_line += line[i] if i < len(line) else ''
                i += 1
            
            if cur_line:
                if not_append:
                    output[-1] += cur_line
                    continue
                output.append(cur_line)
        
        return output
