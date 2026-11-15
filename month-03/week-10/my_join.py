import geopandas as gpd

polygons = gpd.read_file("analysis_ready.gpkg", layer="maiduguri_clipped")

points = gpd.read_file("data/processed/my_points.gpkg", layer="my_points")


joined = gpd.sjoin(polygons, points, how="left", predicate="intersects")

print("Original polygons:", len(polygons))
print("Polygons after join:", len(joined))

print(joined.head())