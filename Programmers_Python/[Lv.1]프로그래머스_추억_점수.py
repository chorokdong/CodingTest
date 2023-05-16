# https://school.programmers.co.kr/learn/courses/30/lessons/176963?language=python3

def solution(name, yearning, photos):
    score = {} # 점수판
    for idx, i in enumerate(name):
        score[i] = yearning[idx] # 인물별 점수 정보 삽입
    
    value_list = []
    for photo in photos:
        value = 0
        for i in photo: # photo 안에 들어있는 인물 하나씩 확인
            if i in score.keys():
                value += score[i] # 인물의 점수를 더해주기
        value_list.append(value)
        
    return value_list