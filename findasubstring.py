first = input()
second = input()
output = ''
for i in range(0, len(first)-len(second) + 1):
    if second == first[i:i+len(second)]:
        output += str(i) + ' '

if output == '':
    output = -1

print(output)
