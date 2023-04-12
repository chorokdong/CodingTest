

class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

    def init_list():
        global node_A # 첫 시작 포인트 이기 때문에 global로 설정
        node_A = Node('A')
        node_B = Node('B')
        node_C = Node('C')
        node_D = Node('D')
        node_A.next = node_B
        node_B.next = node_C
        node_C.next = node_D
        
    def print_list():
        global node_A
        node = node_A
        while node :
            print(node.data)    
            node = node.next

Node.init_list()
# Node.print_list() # A -> B -> C -> D

def insert_node(data):
    global node_A
    new_node = Node(data)
    # 현재 노드 정보를 1,2에 각각 넣고
    node_1 = node_A
    node_2 = node_A
    
    # 새 노드를 삽입할 위치를 계산
    while node_2.data <= data:
        node_1 = node_2
        node_2 = node_2.next
    
    # node_1과 node_2 사이의 새 노드를 연결
    new_node.next = node_2
    node_1.next = new_node


def delete_node(del_data):
    global node_A
    pre_node = node_A
    next_node = pre_node.next
    
    if pre_node.data == del_data:
        node_A = next_node
        del pre_node
        return
    
    while next_node:
        if next_node.data == del_data:
            # 연결 목록에서 next_node를 제거하는 셈
            pre_node.next = next_node.next
            del next_node
            break
        pre_node = next_node
        next_node = next_node.next

    
delete_node('C')    
Node.print_list() # A -> B -> D

insert_node('C')
Node.print_list() # A -> B -> C -> D