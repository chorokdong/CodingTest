

from collections import deque

def BFS(graph, start):
    visited = [] # 방문 노드를 추적
    queue = deque([start]) # 시작 노드 지정
    
    while queue:
        node = queue.popleft() # 가장 왼쪽 노드를 제거하고 반환
        
        if node not in visited: 
            visited.append(node) # 현재 노드 방문 표시
            queue.extend(graph[node])
            
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

print(BFS(graph, 'A'))
# ['A', 'B', 'C', 'D', 'G', 'H', 'I', 'E', 'F', 'J']

