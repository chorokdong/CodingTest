# https://school.programmers.co.kr/learn/courses/30/lessons/42576

# 단 한명을 제외하고 모두 완주
# 참여한 선수들의 이름이 담긴 배열과 완주한 선수들의 이름이 담긴 배열이 주어질 때
# 완주하지 못한 선수의 이름을 return
# 참가자는 동명이인이 존재할 수 있음


# 정확성 테스트는 통과하나 효율성 테스트에서 실패
def solution(participant, completion):
    for com in completion:
        if com in participant:
            participant.remove(com)
    return participant[0]


# 효율성을 위한 코드
# set을 활용하면 동명이인 문제에서 막혀 Counter 사용
from collections import Counter

def solution(participant, completion):
    
    result = Counter(participant) - Counter(completion)
    result = [str(key) for key, value in result.items()]
    
    return result[0]