# https://school.programmers.co.kr/learn/courses/30/lessons/118666

def solution(survey, choices):
    scores = {'R' : 0, 'T' : 0,
              'C' : 0, 'F' : 0,
              'J' : 0, 'M' : 0,
              'A' : 0, 'N' : 0,}
    
    # 성격 점수 매기기
    for sur, cho in zip(survey, choices):
        if cho == 1:
            scores[sur[0]] += 3
        elif cho == 2:
            scores[sur[0]] += 2
        elif cho == 3:
            scores[sur[0]] += 1
        elif cho == 4:
            scores[sur[0]] += 0
        elif cho == 5:
            scores[sur[1]] += 1
        elif cho == 6:
            scores[sur[1]] += 2
        else:
            scores[sur[1]] += 3
    
    # 유형 판단
    def check_type(A : str, B : str):
        result = ''
        if scores[A] >= scores[B]:
            result += ''.join(A)
        else:
            result += ''.join(B)
        return result
    
    key = list(scores.keys())
    result = ''

    for i in range(0, len(key), 2):
        result += ''.join(check_type(key[i], key[i+1]))
        
    return result