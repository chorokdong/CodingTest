# 퀵 정렬
'''
- 합병 정렬과 비슷하게 분할 정복 방식을 이용한 정렬 방식

- 가장 많이 사용되는 정렬법이지만 안정성이 떨어지는 단점이 존재 

- 공간 복잡도 : O(n)

- 시간 복잡도 : 평균 = O(nlog_n) / 최악 = O(n^2)
'''

num = [3,2,6,1,124,6124,23,5,78,24,6,50,9]

def quick_sort(num):
    # 재귀 알고리즘의 기본 사례로 배열의 길이가 1보다 작거나 같으면 배열이 이미 정렬된 것
    if len(num) <= 1:
        return num
    
    else:
        pivot = num[0] # 맨 앞을 선택
        left = []
        right = []
        # 선택된 값을 제외하고 배열의 나머지 요소를 반복하고 left와 right로 분할
        for i in range(1, len(num)):
            if num[i] < pivot:
                left.append(num[i]) # left는 pivot 보다 작은 값
            else : 
                right.append(num[i]) # right는 pivot 보다 큰 값
    
    # 재귀 알고리즘 적용
    return quick_sort(left) + [pivot] + quick_sort(right)

print(quick_sort(num))
        