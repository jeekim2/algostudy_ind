#https://programmers.co.kr/learn/courses/30/lessons/64061
def solution(board, moves):
    ansbuff = []
    answer = 0

    for i in range(len(moves)):
        moves[i] = moves[i]-1

    '''
    board[0][0]~[0][4]
    board[1][0]~[1][4]
    ...
    board[4][0]~[4][4]
    '''

    i = 0
    while i < len(moves):

        j = 0
        while board[j][moves[i]] == 0:
            if j < len(board)-1:
                j+=1
            else:
                j = 0
                i+=1

        ansbuff.append(board[j][moves[i]])
        board[j][moves[i]] = 0
        i+=1

        if len(ansbuff)>1:
            if ansbuff[-1]==ansbuff[-2]:
                answer +=2
                ansbuff.pop()
                ansbuff.pop()
    return answer