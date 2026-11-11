n = int(input())
arr = [int(input()) for _ in range(n)]
stack = []

max_length = 0

for i in arr:
    if len(stack) == 0:
        stack.append(i)
    elif stack[-1] == i:
        stack.append(i)
    else:
        length = len(stack)
        if length > max_length:
            max_length = length
        stack = []
        stack.append(i)

if len(stack)>0 and len(stack)>max_length:
    max_length = len(stack)


print(max_length)