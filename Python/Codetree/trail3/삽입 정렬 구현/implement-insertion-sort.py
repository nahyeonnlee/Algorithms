n = int(input())
arr = list(map(int, input().split()))

for i in range(n):
    #키값 설정
    key = arr[i]
    #j = 0,1,..,i-1
    for j in range(0,i):
        #key보다 큰 값이 arr[j] 
        #즉 key가 arr[j]가 되고 arr[j]부턴 한칸씩 민다
        if key < arr[j]:
            #k= i-1,i-2,...,j
                for k in range(i-1,j-1,-1):
                    arr[k+1] = arr[k] 
                arr[j] = key
                break

print(' '.join(map(str,arr)))