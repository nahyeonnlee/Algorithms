n = int(input())
arr = list(map(int, input().split()))

mid_list = []

for i in range(0,n,2):
    #i가 0
    if i == 0:
        mid_idx = 0
    #i가 2,4,6...
    else: 
        mid_idx = i//2 #1,2,3...
    
    #지금까지 읽어들인 값을 정렬
    sort_arr = sorted(arr[0:i+1])
    
    mid_list.append(sort_arr[mid_idx])

print(' '.join(map(str,mid_list)))