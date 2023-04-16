
# 우선 순위 큐 알고리즘
# 노드의 우선순위 대기열을 유지하기 위한 모듈
import heapq 

def dijkstra(graph, start):
    
    # 시작 노드는 0으로 나머지는 무한대로 초기화
    distance = {node : float('inf') for node in graph}
    distance[start] = 0
    
    # 방문해야 하는 노드를 저장하기 위한 우선 순위 대기열(힙) 생성
    # 시작노드와 노드 자체에서 노드의 현재거리로 구성된 튜플 구성
    pq = [(0, start)]
    
    while pq :
        # 큐에서 시작 노드로 부터 가장 작은 거리에 있는 노드를 pop
        (current_dist, current_node) = heapq.heappop(pq)
        # 시작 노드에서 현재 노드까지의 거리를 이미 알고 있는 거리와 비교
        if current_dist > distance[current_node]:
            continue
        
        for neighbor, weight in graph[current_node].items():
            dist = current_dist + weight # 해당 노드를 거쳐갈 때의 거리 값
            
            if dist < distance[neighbor]:
                distance[neighbor] = dist # 이미 알고있는 거리보다 짧으면 갱신
                heapq.heappush(pq, (dist, neighbor)) # 다음 인접 거리를 계산하기 위해 큐에 삽입
                
    return distance

graph = {
    'A': {'B': 8, 'C': 1, 'D': 2},
    'B': {},
    'C': {'B': 5, 'D': 2},
    'D': {'E': 3, 'F': 5},
    'E': {'F': 1},
    'F': {'A': 5}
        }

print(dijkstra(graph, 'A'))
# {'A': 0, 'B': 6, 'C': 1, 'D': 2, 'E': 5, 'F': 6}