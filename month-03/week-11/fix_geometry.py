import geopandas as gpd

# 1. Load the wards data
wards = gpd.read_file("../../data/processed/wards.gpkg", layer="wards")

# 2. Check if all geometries are valid before fixing
valid_before = wards.is_valid.all()
print("Are all geometries valid before fixing?", valid_before)

# 3. Apply the make_valid() function to fix any issues
wards["geometry"] = wards.geometry.make_valid()

# 4. Check validity again after fixing
valid_after = wards.is_valid.all()
print("Are all geometries valid after fixing?", valid_after)