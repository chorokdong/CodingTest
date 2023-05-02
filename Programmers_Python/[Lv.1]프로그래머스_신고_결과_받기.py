# https://school.programmers.co.kr/learn/courses/30/lessons/92334

# 조건 1 : 여러번 신고가 가능하나, 동일한 유저에 대한 신고 횟수는 1회로 처리 -> 중복 없음
# 조건 2 : k번 이상 신고시 정지 사실을 신고한 유저 메일로 발송(처리 유저마다 발송)

def solution(id_list, report, k):
    
    user = {} # 신고 당한 횟수 목록
    value = {} # 신고한 목록
    for i in id_list:
        user[i] = 0
        value[i] = set([]) # 다른 코드 사용시 리스트로 변경 []

    # 유저가 신고한 목록 추가 
    for i in report:
        user_id, report_id = i.split(' ')
        if user_id not in value.keys():
            value[user_id] = set([report_id])
        else :
            value[user_id].add(report_id)
    
    # 유저별 신고 당한 횟수 
    for i in value:
        for j in value[i]:
            if j in user.keys():
                user[j] += 1        
                
    ########## 유저별 신고 목록과 신고 당한 횟수 다른 코드 ##########
    # for i in set(report):
    #     i = i.split()
    #     user[i[1]] += 1
    #     value[i[0]].append(i[1])
    #######################################################
    
    
    
    result = [0] * len(id_list)
    for x,y in user.items(): # 신고 횟수 중 k번이 넘을 경우
        if y >= k:
            for i,j in value.items(): # 신고 목록 중에 신고한 사람을 찾아서 결과를 보고
                if x in j:
                    result[id_list.index(i)] += 1     
    
    return result