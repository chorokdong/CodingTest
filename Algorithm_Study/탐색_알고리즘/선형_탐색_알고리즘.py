# 선형 탐색 알고리즘
'''
- 왼쪽부터 순서대로 확인하는 방식

- 정렬되지 않은 데이터들을 순차적으로 접근하여 원하는 데이터를 찾는 경우 사용

- 시간 복잡도 : $O(n)$

- 장점 
  - 간단하고 구현이 쉬움
  
  - 목록이 작거나 검색하려는 요소가 목록의 시작 부분에 있을 경우 효울적
  - 목록에 대한 순차적 엑세스만 필요하므로 요소를 반복할 수 있는 모든 데이터 컬럭션에서 작업할 수 있음
  
- 단점 

  - 소요시간이 목록의 크기에 따라 선형적으로 증가
  
  - 목록이 크거나 찾고자 하는 요소가 뒷부분에 있을 경우 비효율적
'''

num = [3, 7, -1, 4, 11, 0, 15, 2, 49]


def linear_search(num, target):
    for i in range(len(num)):
        if num[i] == target:
            return i
    return None

print(linear_search(num, 0))
print(linear_search(num, 50))
