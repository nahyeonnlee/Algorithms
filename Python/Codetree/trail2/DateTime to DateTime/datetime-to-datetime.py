a, b, c = map(int, input().split())

total = a*24*60 + b*60 + c
base = 11*24*60 + 11*60 + 11

if total>=base:
    print(total-base)
else:
    print(-1)