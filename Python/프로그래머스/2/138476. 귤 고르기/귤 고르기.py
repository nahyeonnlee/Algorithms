def solution(k, tangerine):
    answer = 0
    t_num = {}
    
    #무게-개수 딕셔너리 만들기
    for t in tangerine:
        if t_num.get(t,0):
            t_num[t] += 1
        else:
            t_num[t] = 1

    #개수 많은대대로 정렬
    t_num = sorted(t_num.values(),reverse=True)
    
    #k개수에서 빼기
    for i in t_num:
        if k>0:
            k -= i
            answer += 1
        else:
            break
        
    return answer
        