import geopandas as gpd
import folium

# --- 1️⃣ 파일 불러오기 ---
nodes = gpd.read_file("/home/seyeon/hakathon/route_rec/map/nodes.geojson")
edges = gpd.read_file("/home/seyeon/hakathon/route_rec/map/edges.geojson")

# --- 2️⃣ 중심 좌표 계산 (노드 평균) ---
center_y = nodes["geometry"].y.mean()
center_x = nodes["geometry"].x.mean()

# --- 3️⃣ Folium 지도 객체 생성 ---
m = folium.Map(location=[center_y, center_x], zoom_start=14)

# --- 4️⃣ 엣지 (선) 레이어 추가 ---
folium.GeoJson(
    edges,
    name="Edges",
    style_function=lambda x: {"color": "blue", "weight": 2},
).add_to(m)

# --- 5️⃣ 노드 (점) 레이어 추가 ---
for _, row in nodes.iterrows():
    folium.CircleMarker(
        location=[row.geometry.y, row.geometry.x],
        radius=3,
        color="red",
        fill=True,
        fill_color="red",
        fill_opacity=0.7,
    ).add_to(m)

# --- 6️⃣ 지도 저장 ---
m.save("network_map.html")

