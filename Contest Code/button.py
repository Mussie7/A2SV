rep = int(input())
for _ in range(rep):
    string = input().strip()
    pointer = 0
    correct = set()
    while pointer < len(string)-1:
        if string[pointer] == string[pointer+1]:
            pointer += 2
        else:
            correct.add(string[pointer])
            pointer += 1
    
    if pointer < len(string):
        correct.add(string[pointer])
    
    print(''.join(sorted(list(correct))))
