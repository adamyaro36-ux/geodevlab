import geopandas as gpd

# Load and reproject data
wards = gpd.read_file("../../data/processed/wards.gpkg", layer="wards").to_crs(epsg=32631)
facilities = gpd.read_file("../../data/processed/facilities.gpkg", layer="facilities").to_crs(epsg=32631)

# Calculate ward area in square kilometers
wards["area_km2"] = wards.area / 1_000_000

# Create 2km buffer around facilities
reach = facilities[["geometry"]].copy()
reach["geometry"] = reach.buffer(2000)

# Dissolve the buffers so they become one single massive shape
# (This prevents issues where buffers overlap each other)
reach = reach.dissolve()

# Overlay the wards and the dissolved reach to find the difference
# (The parts of the wards that do NOT overlap with the 2km buffers)
uncovered = gpd.overlay(wards, reach, how="difference")

# Calculate the uncovered area
uncovered["uncovered_km2"] = uncovered.area / 1_000_000
total_uncovered = uncovered["uncovered_km2"].sum()

print("Total uncovered area (km2):", round(total_uncovered, 2))
