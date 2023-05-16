# https://school.programmers.co.kr/learn/courses/30/lessons/64061

# 1x1 크기의 칸들로 이루어진 N x N의 정사각 격자
# 인형이 없으면 빈칸이며 크레인의 멈춘 위치의 가장 위에 인형을 집어 바구니에 쌓음
# 같은 모양의 인형 2개가 바구니에 연속해서 쌓이면 바구니에서 사라짐
# 인형이 없는곳에서 크레인을 작동시켜도 아무일 없음
# 크레인을 모두 작동시킨 후 터트려저 사라진 인형의 개수를 return

def solution(board, moves):
    ###### board 정렬을 위한 코드 ######
    board.reverse() # 역순으로 뒤집고
    new_board = [[] for i in range(len(board))] # 새로운 빈 리스트
    
    ###### board 안에있는 0값을 지우고 쉽게 pop을 하기 위해 추가 ######
    for i in board:
        for j in range(len(i)):
            if i[j] == 0:
                pass
            else:
                new_board[j].append(i[j])

    ####### moves의 값 만큼 new_board에서 pop을 진행 ######
    bucket = []
    result = 0

    for i in moves:
        try:
            toy = new_board[i-1].pop()
            bucket.append(toy)
        except :
            pass
        
        ####### 2개 이상이고 2개의 값을 비교했을 때 같으면 삭제 #######
        if len(bucket) >= 2 and bucket[-1] == bucket[-2]:
            bucket.pop()
            bucket.pop()
            result += 2

    return result