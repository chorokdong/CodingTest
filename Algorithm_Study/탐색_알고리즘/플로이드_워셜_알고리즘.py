

def floydWarshall(n, graph):
    # 입력 그래프와 같은 크기의 2D 배열의 리스트를 생성하고 무한대로 초기화
    dist = [[float('inf') for _ in range(n+1)] for _ in range(n+1)]
    
    # 연결된 정점의 거리 값을 기존 graph의 값으로 변경
    # i와 j 사이의 거리는 연결하는 가중치로 설정되며, 없을 경우 거리값은 inf
    for i in range(1, n+1):
        for j in range(1, n+1):
            if i == j :
                dist[i][j] = 0

    for i in graph:
        s = i[0]
        e = i[1]
        t = i[2]
        dist[s][e] = t
        
    # 모든 정점 쌍을 반복하고 i와 j사이에 정점 k를 통과할 경우 경로가 더 짧아지는지 확인
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    return dist


n = 4
graph = [[1,2,4],[1,4,5],[2,1,3],[2,3,7],[3,1,5],[3,4,4],[4,3,2]]

print(floydWarshall(n, graph))
# [inf, inf, inf, inf, inf]
# [inf, 0, 4, 7, 5]
# [inf, 3, 0, 7, 8]
# [inf, 5, 9, 0, 4]
# [inf, 7, 11, 2, 0]

