# https://school.programmers.co.kr/learn/courses/30/lessons/72410

# 아이디와 유사한면서 규칙에 맞는 아이디 추천 
# 길이는 3~15사이 
# 알파벳 소문자, 숫자, 빼기, 밑줄, 마침표만 가능 
# 마침표는 처음과 끝에 사용 불가 / 연속 사용 불가
# 7단계 규칙 순차처리

import re 

def solution(new_id):
    # 1. 소문자 변환
    text = new_id.lower() 
    # 2. 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자를 제거
    result = re.sub('[^a-z0-9-_.]', '', text)
    # 3. 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환
    result = re.sub(r"\.{2,}", ".", result)
    # 4. 마침표(.)가 처음이나 끝에 위치한다면 제거
    result = re.sub(r"(^\.)|(\.$)", "", result)
    # 5. 빈 문자열이라면, new_id에 "a"를 대입
    if result.strip() == '':
        result += 'a'
    # 6. 길이가 16자 이상이면, new_id의 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거
    if len(result) >= 16:
        result = result[:15]
        # 6-1. 만약 제거 후 마침표(.)가 new_id의 끝에 위치한다면 끝에 위치한 마침표(.) 문자를 제거
        result = re.sub(r"\.$", "", result)
    # 7. new_id의 길이가 2자 이하라면, new_id의 마지막 문자를 new_id의 길이가 3이 될 때까지 반복해서 끝에 붙임
    while len(result) < 3:
        result += result[-1]
    
    return result