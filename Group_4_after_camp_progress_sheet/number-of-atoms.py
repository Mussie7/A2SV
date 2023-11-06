class Solution:
    def countOfAtoms(self, formula: str) -> str:
        def atomCounter(index):
            counter = Counter()
            while index < len(formula):
                if formula[index] == '(':
                    new_counter, index = atomCounter(index + 1)
                    counter += new_counter
                    continue
                elif formula[index] == ')':
                    index += 1
                    curr_count = ''
                    while index < len(formula) and formula[index].isnumeric():
                        curr_count += formula[index]
                        index += 1
                    if curr_count == '':
                        return counter, index

                    for atom in counter:
                        counter[atom] *= int(curr_count)
                    
                    return counter, index
                
                curr_atom = formula[index]
                curr_count = ''
                index += 1
                while index < len(formula) and (formula[index].isnumeric() or (formula[index].isalpha() and formula[index] != formula[index].upper())):
                    if formula[index].isnumeric():
                        curr_count += formula[index]
                    else:
                        curr_atom += formula[index]
                    
                    index += 1
                
                if curr_count == '':
                    curr_count = '1'
                
                counter[curr_atom] += int(curr_count)
            
            return counter, index
        
        new_formula = []
        counter, _ = atomCounter(0)
        for atom in sorted(counter.keys()):
            if counter[atom] > 1:
                new_formula.append(atom + str(counter[atom]))
            else:
                new_formula.append(atom)
        
        return ''.join(new_formula)