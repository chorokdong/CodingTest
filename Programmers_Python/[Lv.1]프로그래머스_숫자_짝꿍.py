# https://school.programmers.co.kr/learn/courses/30/lessons/131128

from collections import Counter

def solution(X,Y):
    answer = ''
    X = Counter(X)
    Y = Counter(Y)

    for i in X:
        cnt = 0
        if i in Y:
            cnt = min(X[i], Y[i]) # 둘 중 더 작게 나오는 횟수 선택
            answer += str(i) * cnt

    if answer == '':
        return '-1'

    answer = sorted(answer, reverse=True) # 내림차순 정렬
    if answer[0] == '0': # 첫번째 글자가 0으로 시작하는 경우는 뒤에도 0이 붙는다는 의미
        return '0'

    return ''.join(answer)