# 버블 정렬 알고리즘
'''
- 연속된 2개의 인덱스를 비교하여 순서에 따라 정렬하는 방식

- n개의 원소에 대하여 n개의 메모리를 사용하며, 대부분의 상황에서 최악의 시간복잡도를 보인다.

- 공간 복잡도 : O(n)

- 시간 복잡도 : O(n^2)'''

num = [11,234,23,4,1,5,6,2,65,764,825,46,72,47,26,69,793,25,498,245]

def bubble_sort(num):
    n = len(num)
    for i in range(n):
        for j in range(0, n-i-1):
            if num[j] > num[j+1]:
                num[j], num[j+1] = num[j+1], num[j]
    
    return num

print(bubble_sort(num))
