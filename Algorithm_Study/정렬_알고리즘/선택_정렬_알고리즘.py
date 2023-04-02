# 선택 정렬 알고리즘

'''
- 전체 원소들 중에 정렬 위치에 맞는 것을 선택해 해당 위치로 이동시키는 정렬 방식

- 먼저 주어진 리스트 중에 최소값을 찾고 -> 그 값을 맨 앞에 위치한 값과 교체하는 방식으로 진행

- n개의 원소에 대해 n개의 메모리를 사용하기에 데이터를 하나씩 정밀 비교가 가능

- 교환이 많이 이루어져야하는 자료 상태에서 가장 효율적으로 적용될 수 있는 정렬 방식
  내림차순으로 정렬되어 있는 자료를 오름차순으로 재정렬할 때 최적의 효율을 보임 
  
- 이미 정렬된 상태에서 소수의 자료가 추가됨으로써 재정렬하게 되는 때에는 최악의 처리 속도를 보임

- 공간 복잡도 : O(n)

- 시간 복잡도 : O(n^2)'''

num = [3,2,6,1,124,6124,23,5,78,24,6,50,9]

def selection_sort(num):
    n = len(num)
    for i in range(n):
        min_idx = i # 기준 값
        for j in range(i+1, n):
            if num[j] < num[min_idx]: # 기준 값의 오른쪽에 있는 하위 배열에서 가장 작은 요소의 인덱스를 찾음
                min_idx = j # 현재 최소 요소보다 작은 요소를 찾았을 경우 변경 
        num[i], num[min_idx] = num[min_idx], num[i]
    return num

print(selection_sort(num))
