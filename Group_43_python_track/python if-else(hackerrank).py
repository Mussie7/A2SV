if __name__ == '__main__':
    n = int(input().strip())
if not n % 2:
    if 2 <= n <= 5 or n > 20:
        print('Not Weird')
    else:
        print('Weird')
else:
    print('Weird')
