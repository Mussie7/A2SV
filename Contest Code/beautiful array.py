n = int(input())
arr = input().split()

neg = []
pos = []
zero = []

for num in arr:
    if int(num) < 0 and len(neg) < 1:
        neg.append(num)
    elif int(num) > 0:
        pos.append(num)
    else:
        zero.append(num)

print(1, neg[0])
if len(pos) == 0:
    for i in range(len(zero)):
        if int(zero[i]) != 0:
            pos.append(zero[i])
            zero[i] = ''
        
        if len(pos) == 2:
            break
        
print(len(pos), ' '.join(pos).strip())
print(n - len(pos) - len(neg), ' '.join(zero).strip())
