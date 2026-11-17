import geopandas as gpd

# 1. Load your Maiduguri wards
wards = gpd.read_file("../../ward_with_distance.gpkg")

# 2. Check if all geometries are valid
is_valid_before = wards.is_valid.all()
print("Are all ward geometries valid before fixing?", is_valid_before)

# 3. Fix any invalid geometries
# This will repair any broken shapes without deleting data
wards["geometry"] = wards.geometry.make_valid()

# 4. Check validity again
is_valid_after = wards.is_valid.all()
print("Are all ward geometries valid after fixing?", is_valid_after)

# 5. Save the clean, valid wards so they are ready for your final map
wards.to_file("../../data/processed/my_wards_valid.gpkg", driver="GPKG")
print("Saved valid Maiduguri wards to data/processed/my_wards_valid.gpkg")