import osmnx as ox

# 한글 지역 이름 지정
place_name = "동대문구, 서울, 대한민국"

# 산책로에 해당하는 도로 타입만 선택 (footway, path 등)
custom_filter = ('["highway"~"footway|path|pedestrian|steps|track"]')

# 그래프 다운로드
G = ox.graph_from_place(place_name, custom_filter=custom_filter, network_type='walk', simplify=True)

# 노드 데이터프레임
nodes, edges = ox.graph_to_gdfs(G)

# 노드 좌표 예시
print(nodes[['x', 'y']].head())

# 엣지에 포함된 geometry(라인스트링)
print(edges[['geometry']].head())

nodes.to_file("nodes.geojson", driver="GeoJSON")
edges.to_file("edges.geojson", driver="GeoJSON")
