n, m = (map(int, input().split()))
arrayN = list(map(int, input().split()))
arrayM = list(map(int, input().split()))

pointerN = pointerM = 0
mergedArray = []

while pointerN < n or pointerM < m:
    if pointerM >= m:
        mergedArray.append(arrayN[pointerN])
        pointerN += 1
        continue
    
    if pointerN >= n:
        mergedArray.append(arrayM[pointerM])
        pointerM += 1
        continue
    
    if arrayN[pointerN] > arrayM[pointerM]:
        mergedArray.append(arrayM[pointerM])
        pointerM += 1
    elif arrayM[pointerM] > arrayN[pointerN]:
        mergedArray.append(arrayN[pointerN])
        pointerN += 1
    else:
        mergedArray.append(arrayN[pointerN])
        mergedArray.append(arrayM[pointerM])
        pointerN += 1
        pointerM += 1
 
print(*mergedArray)
