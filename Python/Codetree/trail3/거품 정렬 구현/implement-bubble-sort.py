n = int(input())
arr = list(map(int, input().split()))

for i in range(n):
    for j in range(n-1):
        if arr[j] > arr[j+1]:
            temp = arr[j]
            arr[j] = arr[j+1]
            arr[j+1] = temp
            j += 1

print(' '.join(map(str, arr)))