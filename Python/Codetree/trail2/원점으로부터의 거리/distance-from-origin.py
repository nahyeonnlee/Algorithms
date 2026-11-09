n = int(input())
points = [(int(i), tuple(map(int, input().split()))) for i in range(n)]

list=[]

for idx,p in points:
    d = abs(p[0])+abs(p[1])
    list.append((idx,d))


list.sort(key=lambda x:x[1])

for i in range(n):
    print(list[i][0]+1)