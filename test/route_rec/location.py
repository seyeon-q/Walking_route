import geopandas as gpd

# GeoJSON 파일 경로
file_path = "~/hakathon/route_rec/export.geojson"

# GeoJSON 파일 읽기
gdf = gpd.read_file(file_path)

# 전체 bounds 구하기
minx, miny, maxx, maxy = gdf.total_bounds

print(f"경도 범위: {minx} ~ {maxx}")
print(f"위도 범위: {miny} ~ {maxy}")
