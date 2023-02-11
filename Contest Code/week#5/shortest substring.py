from collections import Counter

rep = int(input())
for _ in range(rep):
    string = input().strip()
    left = 0
    charArray = [0] * 4
    substring = len(string)
    
    for i in range(len(string)):
        while charArray.count(0) == 1:
            substring = min(substring, i - left)
            charArray[int(string[left])] -= 1
            left += 1
        
        if substring == 3:
            break
        
        charArray[int(string[i])] += 1
        
    
    while charArray.count(0) == 1:
        substring = min(substring, len(string)-left)
        charArray[int(string[left])] -= 1
        left += 1
    
    if len(Counter(string)) < 3:
        print(0)
    else:
        print(substring)
