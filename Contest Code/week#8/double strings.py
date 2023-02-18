from collections import Counter

rep = int(input())
for _ in range(rep):
    n = int(input())
    strings = []
    counter = Counter()
    for _ in range(n):
        s = input().strip()
        strings.append(s)
        counter[s] += 1
    
    output = []
    for st in strings:
        found = False
        for i in range(1, len(st)):
            if st[:i] in counter and st[i:] in counter:
                found = True
                break
        if found:
            output.append('1')
        else:
            output.append('0')
    
    print(''.join(output))
