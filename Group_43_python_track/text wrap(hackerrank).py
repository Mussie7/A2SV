import textwrap

def wrap(string, max_width):
    paragraph = ''
    for i in range(len(string)):
        paragraph += string[i]
        if not (i+1) % max_width:
            paragraph += '\n'
    return paragraph

if __name__ == '__main__':
  string, max_width = input(), int(input())
  result = wrap(string, max_width)
  print(result)
