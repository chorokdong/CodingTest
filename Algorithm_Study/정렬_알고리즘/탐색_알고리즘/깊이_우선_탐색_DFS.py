
def DFS(graph, start):
    visited = [] # 방문 노드 추적을 위한 set
    stack = [start] # 시작 노드를 지정 
    
    while stack: # 모든 노드를 방문하는 루프   
        # 후입선출 구조로 스택에 추가된 마지막 노드를 가장 먼저 처리
        node = stack.pop() 
        
        # 현재 노드의 방문 여부 확인
        if node not in visited: 
            visited.append(node) # 미방문의 경우 추가 
            # graph라는 사전에서 현재 노드의 이웃을 가져오기
            # 노드를 key로, 이웃을 value로 가짐
            neighbors = graph[node]  # 즉, node의 이웃 목록을 반환
            stack.extend(neighbors)
    
    return visited


graph = dict()
 
graph['A'] = ['B', 'C']
graph['B'] = ['A', 'D']
graph['C'] = ['A', 'G', 'H', 'I']
graph['D'] = ['B', 'E', 'F']
graph['E'] = ['D']
graph['F'] = ['D']
graph['G'] = ['C']
graph['H'] = ['C']
graph['I'] = ['C', 'J']
graph['J'] = ['I']

print(DFS(graph, 'A'))
# ['A', 'C', 'I', 'J', 'H', 'G', 'B', 'D', 'F', 'E']

