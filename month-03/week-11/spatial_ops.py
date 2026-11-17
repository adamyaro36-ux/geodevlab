import geopandas as gpd

# Load and reproject both layers to UTM
wards = gpd.read_file("../../data/processed/wards.gpkg", layer="wards").to_crs(epsg=32631)
facilities = gpd.read_file("../../data/processed/facilities.gpkg", layer="facilities").to_crs(epsg=32631)

# Create a 2000 meter (2km) buffer around facilities
reach = facilities.copy()
reach["geometry"] = facilities.buffer(2000)
print("Buffered", len(reach), "facilities")

# Count facilities per ward using a spatial join
joined = gpd.sjoin(
    facilities, wards[["ward_name", "geometry"]], how="inner", predicate="within"
)

# Group by ward name and count
counts = joined.groupby("ward_name").size().rename("facility_count").reset_index()

# Merge the counts back to the original wards layer
wards = wards.merge(counts, on="ward_name", how="left")
wards["facility_count"] = wards["facility_count"].fillna(0).astype(int)
print(wards[["ward_name", "facility_count"]])

# Check the total
print("Total counted:", wards["facility_count"].sum(), "of", len(facilities))