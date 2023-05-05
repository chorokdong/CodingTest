# https://school.programmers.co.kr/learn/courses/30/lessons/133499

# "aya", "ye", "woo", "ma" 4가지와 4가지 조합만 사용

def solution(babbling):
    result = 0

    for word in babbling:    
        check_word = ''
        say = ["aya", "ye", "woo", "ma" ]

        for i in word:
            check_word += ''.join(i)

            if check_word in say:
                say = ["aya", "ye", "woo", "ma" ]
                say.remove(check_word)
                check_word = ''        

            else:
                pass

        if check_word.strip() == '':
            result += 1
    return result

'''이 문제의 핵심은 다시 발음할 수 있나의 여부인듯하다. 
   처음 문제를 이해했을 때에는 한번 발음을 하면 다시 발음을 못한다고 이해를 하였다.
   그로인해 테스트 케이스 4가지 정도에서 오류가 발생했고 이를 수정하기 위해 
   16번째 줄에 발음 가능한 리스트들을 다시 넣어주어 문제를 해결했다.'''
   
# babbling = ["ayayeye"] -> 0
# babbling = ["ayayeayayeayaaya"] -> 0 
# babbling = ["ayayeaya"] -> 1 (연속으로 같은 발음만 아니면 다시 사용 가능)