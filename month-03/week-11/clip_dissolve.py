import geopandas as gpd

# 1. Load and reproject data
wards = gpd.read_file("../../data/processed/wards.gpkg", layer="wards").to_crs(epsg=32631)
roads = gpd.read_file("../../data/processed/roads.gpkg").to_crs(epsg=32631)

# --- PART 1: CLIP ---
# Let's isolate just the "Agodi" ward
agodi_ward = wards[wards["ward_name"] == "Agodi"]

# Clip the roads so we only have the parts that fall inside Agodi
roads_in_agodi = gpd.clip(roads, agodi_ward)

print("--- CLIP RESULTS ---")
print("Total road features in whole dataset:", len(roads))
print("Road features clipped to just Agodi:", len(roads_in_agodi))


# --- PART 2: DISSOLVE ---
# Merge all 12 wards into one single polygon (LGA boundary)
lga_outline = wards.dissolve()

print("\n--- DISSOLVE RESULTS ---")
print("Original number of wards:", len(wards))
print("Number of features after dissolve:", len(lga_outline))