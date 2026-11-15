import pandas as pd
import geopandas as gpd

table = pd.read_csv("P_stations.csv")
print(table.head(3))

facilities = gpd.GeoDataFrame(
    table,
    geometry=gpd.points_from_xy(table["Northing"], table["Easting"]),
    crs="EPSG:32632"
)

facilities.to_file("data/processed/my_points.gpkg", layer="my_points")
print("Saved", len(facilities), "points")