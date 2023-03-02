# the function I wrote
def superDigit(n: str, k: int) -> int:
    newNum = 0
    for digit in str(n):
        newNum += int(digit)
    newNum *= k
    
    if len(str(newNum)) == 1:
        return newNum
    
    return superDigit(newNum, 1)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = first_multiple_input[0]

    k = int(first_multiple_input[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()
