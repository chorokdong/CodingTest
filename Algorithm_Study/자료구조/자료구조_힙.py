class Heap:
    def __init__(self):
        self.heap = []
    
    # Heap에 값 추가
    def push(self, value):
        self.heap.append(value)
        # 힙의 끝에 새 요소를 추가한 후 힙 속성을 유지하는데 사용하는 방식
        self._sift_up(len(self.heap) - 1)
        
    # Heap에서 최소값을 제거하고 반환
    def pop(self):
        if not self.heap: 
            return None # 비어있다면 None 반환
        # 최소값을 힙의 마지막 값과 교체 후
        self._swap(0, len(self.heap) - 1) 
        # 마지막값 제거
        value = self.heap.pop()     
        # 교체된 값을 Heap의 올바른 위치로 이동 
        self._sift_down(0)
        return value
    
    # 인덱스 i가 주어지면 힙 속성에 따라 올바른 위치에 갈 때까지 해당 인덱스의 값을 힙 위로 이동
    def _sift_up(self, i):
        # 인덱스 i에서 요소의 부모 인덱스를 찾음
        parent = self._parent(i)
        # 부모 값이 인덱스 i의 값 보다 크면 
        if i > 0 and self.heap[parent] > self.heap[i]:
            # 두 값을 교환
            self._swap(i,parent)
            # 올바른 위치까지 재귀적 반복
            self._sift_up(parent)
            
    def _sift_down(self, i):
        min_index = i
        # 자식의 인덱스가 힙의 길이보다 작고, min_index의 값보다 작으면 왼쪽(오른쪽) 자식의 인덱스로 업데이트
        left = self._left_child(i)
        if left < len(self.heap) and self.heap[left] < self.heap[min_index]:
            min_index = left
        
        right = self._right_child(i)
        if right < len(self.heap) and self.heap[right] < self.heap[min_index]:
            min_index = right
        
        # 최소값이 인덱스 i에 없으면 i와 min_index의 값을 교환하고
        # 최소값의 인덱스에서 재귀적 호출
        if i != min_index:
            self._swap(i, min_index)
            self._sift_down(min_index)
            
    # 인덱스 i에 있는 노드의 부모 노드의 인덱스를 반환
    def _parent(self, i):
        return (i - 1) // 2
    
    # 인덱스 i에 있는 노드의 왼쪽 자식 인덱스를 반환
    def _left_child(self, i):
        return 2 * i + 1
    
    # 인덱스 i에 있는 노드의 오른쪽 자식 인덱스를 반환
    def _right_child(self, i):
        return 2 * i + 2

    # 인덱스 i와 j의 값을 교환
    def _swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

value_list = [5, 1, 50, 3, 19, 11]

heap = Heap()

for i in value_list:
    heap.push(i)
    
print(heap.heap) # [1, 3, 11, 5, 19, 50]

# 루트 노드 : 1
# 루트 노드의 자식 노드 : 3(왼쪽) 11(오른쪽)
# 왼쪽 노드 3의 자식 노드 : 5(왼쪽)
# 오른쪽 노드 11의 자식 노드 : 19(왼쪽) 50(오른쪽)

#       1
#   3       11 
# 5   -  19   50