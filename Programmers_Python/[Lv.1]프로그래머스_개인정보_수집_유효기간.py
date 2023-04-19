# 조건 1 : 개인정보는 유효기간 전까지만 보관, 지났다면 파기
# 조건 2 : 모든 달은 28일까지 있다고 가정
# 조건 3 : 오늘 날짜별로 파기해야할 개인정보 번호를 구하라
# 조건 4 : DD가 한 자릿수일 경우 앞에 0이 붙음
import datetime 

def solution(today, terms, privacies):
    pri_list = []
    ter_list = []
    for i in privacies:
        time, term = i.split(' ')
        year,month, day = time.split('.')
        pri_list.append(term)
        ter_list.append([int(year), int(month), int(day)])

    # 약관별 보유제한 기간 
    for i in terms:
        term, month = i.split(' ')
        if term in pri_list: # 제한기간에 대한 내용이 보유한 약관 리스트 중에 있다면 
            list_idx = [i for i, j in enumerate(pri_list) if j == term ] # 인덱스 번호를 반환

            if len(list_idx) >= 2: # 2개 이상 반환시
                for i in list_idx:
                    ter_list[i][1] += int(month)
            else: # 1개 반환시
                ter_list[list_idx[0]][1] += int(month)

    # 연월일 값 수정
    for i in ter_list:
        if i[1] > 12:
            i[1] -= 12
            i[0] += 1

    y,m,d = map(int,today.split('.'))
    TODAY = datetime.datetime(y,m,d)
    TODAY

    result = []
    for i, idx in enumerate(range(len(ter_list))):
        if TODAY >= datetime.datetime(ter_list[i][0],ter_list[i][1],ter_list[i][2]):
            result.append(idx + 1)
    
    return result


#################### 년,월,일을 일로 치환 ####################
def solution(today, terms, privacies):
    y,m,d = today.split('.')
    today = int(y) * 12 * 28 + int(m) * 28 + int(d)

    value = {}
    for i in terms:
        term, month = i.split(' ')
        value[term] = int(month) * 28

    result = []
    for idx, i in enumerate(privacies):
        time, term = i.split(' ')
        y, m , d = time.split('.')
        DAY = int(y) * 12 * 28 + int(m) * 28 + int(d)
        if DAY + value[term] <= today:
            result.append(idx + 1)

    return result