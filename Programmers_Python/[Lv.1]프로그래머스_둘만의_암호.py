# https://school.programmers.co.kr/learn/courses/30/lessons/155652

# 조건 1: 문자열 s의 각 알파벳을 index 만큼 뒤의 알파벳으로 바꿈
# 조건 2: index 만큼 뒤로 이동했을 때 z를 넘는다면 다시 a로 돌아옴
# 조건 3: skip에 있는 알파벳은 건너뜀


def solution(s, skip, index):
    alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

    ##### 삭제할 알파벳의 인덱스값 추출 #####
    del_num = []
    for i in skip:
        if i in alpha:
            del_num.append(alpha.index(i))

    ##### 알파벳 삭제 #####
    alpha = [alpha[i] for i in range(len(alpha)) if i not in del_num]

    ##### index 값 만큼 뒤로 이동 
    result = []
    for i in s:
        for j in range(len(alpha)):
            if i == alpha[j]:
                if j + index >= len(alpha):
                    value = (j + index) % len(alpha)  # 처음에 (j + index) - len(alpha)로 설정했는데 
                    result.append(value)              # 그렇게 하면 값이 넘어가면 에러가 발생해 %로 수정
                else :
                    result.append(j + index)

    ##### 뒤로 이동한 값을 토대로 문자 생성 #####
    value = ''
    for i in result:
        value += ''.join(alpha[i])
        
    return value

################################## 짧은 풀이법 ##################################
from string import ascii_lowercase # 알파벳 소문자 전체 str 값

def solution(s, skip, index):

    alpha = set(ascii_lowercase)
    alpha -= set(skip)
    alpha = sorted(alpha)


    dic_alpha = {i : idx for idx, i in enumerate(alpha)}

    result = ''
    for i in s:
        result += alpha[(dic_alpha[i] + index) % len(alpha)]
    
    return result
    