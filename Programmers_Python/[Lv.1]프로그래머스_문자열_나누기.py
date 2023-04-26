# https://school.programmers.co.kr/learn/courses/30/lessons/140108

# 첫 글자(x)를 오른쪽 방향으로 읽고 x와 x가 아닌 횟수를 계산
# 처음 두 횟수가 같아질 경우 멈추고 문자열 분리
# 분리 후 남은 문자열에서 위 과정 반복 (없다면 종료)
# 횟수가 다른데 읽을 문자가 없다면, 문자열 분리하고 종료

def solution(s):

    result = 0
    t = ['', 0, 0]

    for word in s:
        if t[0] == '':
            t[0] = word # 지정문자
            t[1] += 1 # 지정문자수 + 1
        else:
            if t[0] == word: # 지정문자와 비교 문자가 같다면
                t[1] += 1 # 지정문자수 + 1
                
            else: # 지정문자와 비교 문자가 다르다면
                t[2] += 1 # 비교문자수 + 1
                
            if t[1] == t[2]: # 지정문자수와 비교 문자수가 같다면
                result += 1
                t = ['', 0, 0] # 리셋

    if t != ['', 0, 0]: # 더 이상 읽을 문자가 없다면
        result += 1
    
    return result 