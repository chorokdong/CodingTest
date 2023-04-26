# https://school.programmers.co.kr/learn/courses/30/lessons/161990

# 조건1 : 정사각형 격자판이며, 좌상단 (0,0)
# 조건2 : 빈칸 = . / 파일 존재 = #
# 조건3 : 최소한의 드래그(이동거리)로 모든 파일을 선택해서 삭제를 원함
# 조건4 : S(lux,luy)에서 E(rdx, rdy)로 드래그는 |rdx - lux| + |rdy - luy|

# 풀이과정: 주어진 wallpaper에서 반복문을 돌아 좌상단, 좌하단, 우상단, 우하단에 결리는 #의 값을 체크 
# (단, 격자 기준 좌상단을 찾기 때문에 우상단과 우하단 값에는 각각 +1 씩 해줘야함)

def solution(wallpaper):
    
    # 파일이 있는(#) 좌표 찾기
    value = []
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[i])):
            if wallpaper[i][j] == '#':
                value.append([i,j])

    # 각 파일의 제일 끝점 찾기                
    col_list = []
    row_list = []
    for i in value: 
        col_list.append(i[0])
        row_list.append(i[1])
    
    min_row, max_row = min(row_list), max(row_list)
    min_col, max_col = min(col_list), max(col_list)
    
    # 가장 우측과 가장 하단의 경우 +1씩 더해줘야 함 
    value = [min_col, min_row, max_col + 1, max_row + 1]        
    
    return value