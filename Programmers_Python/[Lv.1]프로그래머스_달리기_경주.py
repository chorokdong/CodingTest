# https://school.programmers.co.kr/learn/courses/30/lessons/178871

# 이름을 부르면 해당 선수가 앞 선수를 추월 
# 즉, 이름 부른 선수와 앞 선수의 순위가 바뀜

def solution(players, callings):
    for call in callings:
        num = players.index(call)
        players[num - 1], players[num] = players[num], players[num - 1]
    
    return players

'''위 코드는 시간 복잡도 문제로 인해 시간 초과 에러가 발생한다.
   7번째, 8번째 줄에서는 callings 배열(크기:M)과 players 배열(크기:N)의 크기에 비례하기 때문에 시간복잡도는 둘의 곱인 O(MN)이 된다. 
   일반적으로 O(n)에서 n의 값이 1억을 넘으면 통과가 어렵다고 보면 되는데, 
   문제 조건을 보면 100만 * 5만 = 500억 이라는 수가 나오게 되어 에러가 발생한다.'''

###################### 수정한 방법 1 (dict 2개) ######################
def solution(players, callings):

    player_to_idx = {player : idx for idx, player in enumerate(players)}
    idx_to_player = {idx : player for idx, player in enumerate(players)}

    for call in callings:
        current_num = player_to_idx[call] # 현재 선수 위치
        front_num = current_num - 1 # 앞 선수의 위치

        current_player = call # 현재 선수 = 호명한 선수
        front_player = idx_to_player[front_num] # 현재 선수의 앞 선수

        player_to_idx[current_player] = front_num # 현재 선수는 앞 선수의 위치로 가고
        player_to_idx[front_player] = current_num # 앞 선수는 현재 선수의 위치로 간다.

        # idx_to_player도 동일하게 순서 변경
        idx_to_player[current_num] = front_player
        idx_to_player[front_num] = current_player
    
    return list(idx_to_player.values())
    
###################################################################

###################### 수정한 방법 2 (dict 1개) ######################
def solution(players, callings):
    player_idx= {player : idx for idx, player in enumerate(players)}


    for call in callings:
        current_num = player_idx[call] # 현재 선수 위치
        front_num = current_num - 1 # 앞 선수 위치

        players[front_num], players[current_num] = players[current_num], players[front_num]

        player_idx[players[current_num]] = current_num
        player_idx[players[front_num]] = front_num

    return players
###################################################################

# dict의 개수가 적을 수록 더 적은 시간복잡도를 가진다