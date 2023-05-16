# https://school.programmers.co.kr/learn/courses/30/lessons/67256

# 왼손은 * 오른손은 # 시작
# 상하좌우 4가지 방향으로만 이동가능
# 1, 4, 7 입력시에는 왼손 사용 
# 3, 6, 9 입력시에는 오른손 사용
# 가운데 2, 5, 8, 0 입력시에는 더 가까운 손 사용
# 거리가 같다면 오른손잡이는 오른손, 왼손 잡이는 왼손 사용

from math import*

def solution(numbers, hand):
    keypad = { 1 : [1,1], 2 : [1,2], 3 : [1,3],
               4 : [2,1], 5 : [2,2], 6 : [2,3],
               7 : [3,1], 8 : [3,2], 9 : [3,3],
               10 : [4,1], 0 : [4,2], 11 : [4,3]}

    # 맨하탄 거리
    def manhattan_distance(x, y):
        return sum(abs(a-b) for a,b in zip(x,y))

    left_hand = 10
    right_hand = 11

    result = ''
    for i in numbers:
        if i in [1,4,7] :
            result += ''.join('L')
            left_hand = i # 왼손의 위치

        elif i in [3,6,9] :
            result += ''.join('R')
            right_hand = i # 오른손의 위치

        else:
            if manhattan_distance(keypad[left_hand], keypad[i]) > manhattan_distance(keypad[right_hand], keypad[i]):
                result += ''.join('R')
                right_hand = i

            elif manhattan_distance(keypad[left_hand], keypad[i]) < manhattan_distance(keypad[right_hand], keypad[i]):
                result += ''.join('L')
                left_hand = i

            else:
                if hand == 'right':
                    result += ''.join('R')
                    right_hand = i
                    
                else:
                    result += ''.join('L')
                    left_hand = i

    return result