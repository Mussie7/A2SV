# Enter your code here. Read input from STDIN. Print output to STDOUT
rep = int(input())
dic, output = {}, []
for _ in range(rep):
    st = input()
    if st in dic:
        dic[st] += 1
    else:
        output.append(st)
        dic[st] = 1

st_output = ""
for i in range(len(output)):
    st_output += str(dic[output[i]]) + " "

print(str(len(output)))
print(st_output[:-1])
