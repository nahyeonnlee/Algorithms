n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

list = [0 for _ in range(101)]

for seg in segments:
    for i in range(seg[0], seg[1]+1):
        list[i] += 1

print(max(list))
    
