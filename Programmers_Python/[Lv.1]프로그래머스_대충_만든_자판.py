# 설명 1 : 키의 개수가 1 ~ 100개 
# 설명 2 : 같은 문자가 자판에 여러번 할당 / 키 하나에 문자가 여러번 할당 / 할당되지 않는 경우도 존재 


def solution(keymap, targets):

    # targets에서 한 단어씩 주어진 keymap에서 비교를해 여러가지 keymap 중 더 작은 값을 value에 추가
    # inf가 없다면 모두 더해서 최소횟수를 찾아내고
    result = []
    for target in targets:
        value = []
        for i in target: 
            num = float('inf')
            for key in keymap: 
                try:
                    if num > key.index(i): 
                        num = key.index(i) 
                except:
                    continue
            value.append(num + 1)        
        result.append(value)     

    # inf가 있다면 해당 값을 -1로 변경
    final_result = []
    for value in result:
        if float('inf') in value:
            final_result.append(-1)
        else:
            final_result.append(sum(value))  
        
    return final_result


################################## 잘못된 풀이 ##################################
# Why? 지문을 잘못읽었다. 지문에는 자판을 통해서 원하는 문장을 만들지 못한다면 -1을 도출하라고 하였지만
# 나의 경우 만들지 못하는 문장을 제외하고 최소횟수를 도출하려고 하였다. 

def solution(keymap, targets):
    result = []
    for target in targets:
        value = []
        for i in target:
            num = float('inf')
            for key in keymap:
                try:
                    if num > key.index(i):
                        num = key.index(i) 
                except:
                    continue
            value.append(num + 1)        
        result.append(value)     

    final_result = []
    for value in result:
        change = [i for i, ele in enumerate(value) if ele == float('inf')]
        if len(value) == len(change):
            value = [-1]
        else:
            for i in range(len(value)):
                if value[i] == float('inf'):
                    value[i] = 0
        final_result.append(sum(value))    
        
    return final_result
