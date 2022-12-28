class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        files = defaultdict(list)

        for path in paths:
            directory = path.split()
            for i in range(1, len(directory)):
                index = directory[i].find('(')
                files[directory[i][index:]].append(directory[0] + '/' + directory[i][:index])
        
        output = []
        for duplicate in files:
            if len(files[duplicate]) > 1:
                output.append(files[duplicate])
        
        return output
