n, k, t = input().split()
n, k = int(n), int(k)
str = [input() for _ in range(n)]

startwith = []
len_t = len(t)

for s in str:
    if s[0:len_t] == t:
        startwith.append(s)

startwith.sort()

print(startwith[k-1])