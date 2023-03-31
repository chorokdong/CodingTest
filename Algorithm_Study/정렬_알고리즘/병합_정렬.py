# 병합 정렬
'''
- 분할 정복(큰 문제를 반으로 쪼개어 해결해 나가는 방식) 방식을 이용한 정렬 방식

- 분할 정복 방식에 의해 큰 배열을 크기가 1이 될때가지 반으로 자른 후 잘린 배열을 정렬하여 합침

- 공간 복잡도 : O(n)

- 시간 복잡도 : O(nlog_n)
'''

num = [3,2,6,1,124,6124,23,5,78,24,6,50,9]

def merge_sort(num):
    if len(num) <= 1:
        return num
    else: 
        mid = len(num) // 2 # 중간값 찾기
        left = num[ : mid ] # 분할
        right = num[ mid : ] # 분할 
        left = merge_sort(left) # 재귀적용
        right = merge_sort(right) # 재귀적용 
        return merge(left, right) # 병합 알고리즘 적용
    
def merge(left, right):
    result = []
    # left와 right의 시작 포인트
    i = 0
    j = 0 
    while i < len(left) and j < len(right):
        # 두 포인터가 가리키는 요소를 비교하고 더 작은 요소를 result 배열에 추가
        # 이후 더 작은 요소를 포함하는 하위 배열의 포인터를 다음 인덱스로 이동
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    # 하위 배열 중 하나가 완전히 처리된 후 다른 하위 배열의 나머지 요소를 result 배열에 추가
    # while 루프가 완료된 후 하위 배열 중 아직 result에 추가되지 않은 일부요소가 남아있을 수 있음
    # 그렇기 때문에 두 하위 배열의 모든 요소가 result 배열에 추가해야 됨
    result += left[i : ]
    result += right[j : ]
    return result

print(merge_sort(num))