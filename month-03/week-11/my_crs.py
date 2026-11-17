import pandas as pd
import geopandas as gpd

# 1. Load the CSV file
# We use ../../ because the file is at the root of the project
df = pd.read_csv("../../P_stations.csv")

# 2. Convert to a GeoDataFrame using Easting (X) and Northing (Y)
# CRS is set to EPSG:32633 (UTM Zone 33N for Maiduguri)
gdf = gpd.GeoDataFrame(
    df, 
    geometry=gpd.points_from_xy(df['Easting'], df['Northing']),
    crs="EPSG:32633"
)

print("Original CRS:", gdf.crs)

# 3. Ensure it is in EPSG:32633 (it already is, but this is good practice)
gdf_utm = gdf.to_crs(epsg=32633)
print("Final CRS:", gdf_utm.crs)

# 4. Save the projected version as a GeoPackage so we can map it later
gdf_utm.to_file("../../data/processed/my_stations_utm.gpkg", driver="GPKG")
print("Saved police stations to data/processed/my_stations_utm.gpkg")