# https://school.programmers.co.kr/learn/courses/30/lessons/172928

# 조건1 : 이동시 공원을 벗어나거나면 해당 명령 무시
# 조건2 : 이동시 장애물을 만나면 장애물에 걸린것 처럼 해당 명령을 제외한 명령만 따름
# 조건3 : 좌상단은 (0,0), 우하단은 (H-1, W-1) ==> 0 부터 시작을 의미

def solution(park, routes):
    
    start = []
    # 시작점 찾기
    for i in range(len(park)):
            if 'S' in park[i]:
                start = [i, park[i].find('S')]
                break
                
    for route in routes:
        dir, move = route.split(' ')
        move = int(move)
        
        if dir == 'E':
            loc = start[1] + move
            if loc >= len(park[0]): # 경계를 넘어간다면
                continue
            if 'X' in park[start[0]][start[1]+1 : loc + 1]: # 장애물이 있다면
                continue
            else:
                start[1] = loc
                
        if dir == 'W':
            loc = start[1] - move
            if loc < 0 :
                continue
            if 'X' in park[start[0]][loc : start[1]]:
                continue
            else : 
                start[1] = loc 
        
        if dir == 'S':
            loc = start[0] + move
            if loc >= len(park):
                continue
            # 행을 바꿔가며 확인해야 하기 때문에 반복문 필요    
            if 'X' in [park[i][start[1]] for i in range(start[0] + 1, loc + 1)]:
                continue
            else:
                start[0] = loc        
                
        if dir == 'N':
            loc = start[0] - move
            if loc < 0 :
                continue
            if 'X' in [park[i][start[1]] for i in range(loc, start[0])]:
                continue
            else:
                start[0] = loc
                
    return start
                            
                