import geopandas as gpd

# 1. Load and reproject both layers to UTM (meters)
wards = gpd.read_file("../../data/processed/wards.gpkg", layer="wards").to_crs(epsg=32631)
facilities = gpd.read_file("../../data/processed/facilities.gpkg", layer="facilities").to_crs(epsg=32631)

# 2. Get the center point of each ward (centroid)
# This ensures we measure from the middle of the ward, not the edge
wards_centroids = wards.copy()
wards_centroids["geometry"] = wards_centroids.centroid

# 3. Find the nearest facility for each ward centroid
nearest = gpd.sjoin_nearest(
    wards_centroids, 
    facilities, 
    how="left", 
    distance_col="distance_m"
)

# 4. Print the results
print(nearest[["ward_name", "distance_m"]])
