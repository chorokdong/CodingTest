# https://school.programmers.co.kr/learn/courses/30/lessons/42862

# 바로 앞번호의 학생 or 바로 뒷번호의 학생에게만 빌려줄 수 있음
# 즉 4번은 3,5번에게만 빌려줄 수 있음


def solution(n, lost, reserve): 
    
    answer = 0 
    
    # 여분을 가져온 학생이 분실했을 가능성이 있으며 
    # 해당 학생은 옷을 못 빌려주기 때문에 set의 차집합을 통해 제거 
    reserve_del = set(reserve)-set(lost) 
    lost_del = set(lost)-set(reserve) 
    
    for i in reserve_del: 
        if i-1 in lost_del: 
            lost_del.remove(i-1) 
            
        elif i+1 in lost_del: 
            lost_del.remove(i+1) 
            
    answer = n - len(lost_del)
    
    return answer