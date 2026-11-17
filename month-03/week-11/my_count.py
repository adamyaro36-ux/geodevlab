import geopandas as gpd

# 1. Load your projected police stations
stations = gpd.read_file("../../data/processed/my_stations_utm.gpkg")

# 2. Load your Maiduguri wards and make sure they are in the same projection (UTM 33N)
wards = gpd.read_file("../../ward_with_distance.gpkg").to_crs(epsg=32633)

# 3. Spatial Join: Find which ward each police station is inside
# Note: You need to make sure the column name for your ward names is correct. 
# I am using "ward" because I saw it in your 'wards.csv' screenshot.
joined = gpd.sjoin(stations, wards[["ward", "geometry"]], how="inner", predicate="within")

# 4. Count the stations per ward
counts = joined.groupby("ward").size().rename("police_station_count").reset_index()

print("--- POLICE STATIONS PER WARD ---")
print(counts)