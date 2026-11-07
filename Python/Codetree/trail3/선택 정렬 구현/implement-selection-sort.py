n = int(input())
arr = list(map(int, input().split()))

for i in range(n):
    k = min(arr[i:])
    idx = arr.index(k, i)
    arr[idx] = arr[i]
    arr[i] = k

print(' '.join(map(str,arr)))