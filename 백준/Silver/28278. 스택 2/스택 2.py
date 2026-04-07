import sys

data = sys.stdin.read().split()

n = int(data[0])
stack = []
out = []

i = 1
for _ in range(n):
    c = data[i]
    i += 1
    
    if c == '1':
        stack.append(int(data[i]))
        i += 1
    elif c == '2':
        out.append(str(stack.pop()) if stack else '-1')
    elif c == '3':
        out.append(str(len(stack)))
    elif c == '4':
        out.append('0' if stack else '1')
    else:
        out.append(str(stack[-1]) if stack else '-1')

sys.stdout.write('\n'.join(out) + '\n')