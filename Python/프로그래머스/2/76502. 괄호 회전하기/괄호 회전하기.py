def solution(s):
    answer = 0
    n = len(s)    
    dic = {'[':']', '{':'}', '(':')'}
    
    #x번째 회전 
    for x in range(n):
        stack = []
        #스택에 넣기
        for i in range(n):
            #넣을 값 계산
            current = s[(x+i)%n]
            
            #만약 스택에 값이 있고, 스택 맨 위와 괄호 짝이 맞으면
            if stack and stack[-1] in dic and dic[stack[-1]] == current:
                stack.pop()
            #그 외의 경우 스택에 넣기
            else:
                stack.append(current)
                
        #한 바퀴 돌고 스택에 값이 남아 있는지 여부
        if len(stack)==0:
            answer+=1
        
        
    return answer