# https://school.programmers.co.kr/learn/courses/30/lessons/133502

# 조건 1 : 정해진 순서(빵-야채-고기-빵) 순으로 쌓음
# 조건 2 : 6번째 재료가 쌓이면 3~6 번째 재료를 이용해 버거 만듬
# 조건 3 : 9번째 재료가 쌓이면 2번째 + 7~9번째 재료를 이용해 버거 만듬
# 조건 4 : 빵(1) 야채(2) 고기(3) 빵(1) 순으로 쌓아야함

def solution(ingredient):
    i = 0
    result = 0
    while i <= len(ingredient):
        if ingredient[i : i + 4] == [1,2,3,1]:
            del(ingredient[i : i + 4])        
            i -= 3
            result += 1
        i += 1  

    return result