def solution(board, moves):
    answer = 0
    stack = []
    
    #인형 뽑고 보드에서 제거, 스택에 추가
    for i in moves:
        for j in range(len(board)):
            if board[j][i-1]:
                stack.append(board[j][i-1])
                board[j][i-1] = 0
                break
        
        #지금 넣은 인형이 아래 인형과 같은지
        if len(stack)>1: 
            if stack[-1] == stack[-2]:
                answer+=2
                stack.pop()
                stack.pop()
                
            
    return answer