import math
import os
import random
import re
import sys

# the actual function
def arrayManipulation(n, queries):
    preSum = [0] * (n+2)
    for start, end, value in queries:
        preSum[start] += value
        preSum[end+1] -= value
    
    maxVal = preSum[0]
    for i in range(1, len(preSum)):
        preSum[i] += preSum[i-1]
        maxVal = max(maxVal, preSum[i])
    
    return maxVal

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()
