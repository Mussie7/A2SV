s = input()

left, right = 0, len(s)-1
simple = []
while left < right:
    while left < right and s[left] != '(':
        left += 1
        
    while right > left and s[right] != ')':
        right -= 1
    
    if left < right:
        simple.append(left+1)
        simple.append(right+1)
        left += 1
        right -= 1

if simple:
    print(1)
    print(len(simple))
    print(*sorted(simple))
else:
    print(0)
