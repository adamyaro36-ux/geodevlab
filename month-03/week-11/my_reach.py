import geopandas as gpd

# 1. Load your projected police stations
stations = gpd.read_file("../../data/processed/my_stations_utm.gpkg")

# 2. Create a 2,000-meter (2km) buffer around each station
buffer = stations.copy()
buffer["geometry"] = buffer.buffer(2000)

# 3. Calculate the total area covered by these buffers (in square km)
# We divide by 1,000,000 because our CRS is in meters (square meters to square km)
total_area = buffer.area.sum() / 1_000_000

print("Total area covered by 2km police station buffers (km2):", round(total_area, 2))