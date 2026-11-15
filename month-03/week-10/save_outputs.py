import geopandas as gpd

wards = gpd.read_file("data/processed/wards.gpkg", layer="wards")

# Save as a new GeoPackage layer
wards.to_file("data/processed/week-10_outputs.gpkg", layer="wards_copy")

# Save as a CSV (drop the geometry so it's just a table)
wards.drop(columns="geometry").to_csv("month-03/week-10/wards_table.csv", index=False)

# List the layers to prove it worked
print(gpd.list_layers("data/processed/week-10_outputs.gpkg"))