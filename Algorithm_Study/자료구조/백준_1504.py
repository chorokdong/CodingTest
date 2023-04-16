

################## 백준 1504 ##################
import heapq 

n, m = map(int, input().split()) # 정점의 개수 / 간선의 개수
graph = [[]for i in range(n+1)]

for _ in range(m):
    a, b, w = map(int, input().split()) # a 정점에서 b 정점까지 양방향 길이와 거리의 값 w
    graph[a].append((b,w))
    graph[b].append((a,w))
    
v1, v2 = map(int, input().split()) # 반드시 거쳐야하는 정점 번호

def dijkstra(start):
    
    distance = [float('inf') for _ in range(n+1)]
    distance[start] = 0
    
    pq = [(0, start)]
    
    while pq :
        (current_dist, current_node) = heapq.heappop(pq)
        # 시작 노드에서 현재 노드까지의 거리를 이미 알고 있는 거리와 비교
        if current_dist > distance[current_node]:
            continue
        
        for neighbor, weight in graph[current_node]:
            dist = current_dist + weight # 해당 노드를 거쳐갈 때의 거리 값
            
            if dist < distance[neighbor]:
                distance[neighbor] = dist # 이미 알고있는 거리보다 짧으면 갱신
                heapq.heappush(pq, (dist, neighbor)) # 다음 인접 거리를 계산하기 위해 큐에 삽입       
        
    return distance

total = dijkstra(1) # 1번 부터 n번 까지의 경로값
v1_ = dijkstra(v1) # v1번 부터 n번 까지의 경로값
v2_ = dijkstra(v2) # v2번 부터 n번 까지의 경로값

print(total) # [inf, 0, 3, 5, 4]
print(v1_) # [inf, 3, 0, 3, 4]
print(v2_) # [inf, 5, 3, 0, 1]

cnt = min(total[v1] + v1_[v2] + v2_[n], total[v2] + v2_[v1] + v1_[n])
'''1번 부터 시작해 v1번까지 + v1번 부터 v2까지 + v2번 부터 n번까지
   OR 1번 부터 시작해 v2번까지 + v2번 부터 v1까지 + v1번 부터 n번까지
   경로 중 짧은(최단거리) 거리 계산'''
   
print(cnt if cnt < float('inf') else '-1') # 7 