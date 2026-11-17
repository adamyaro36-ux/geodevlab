import geopandas as gpd
import matplotlib.pyplot as plt

# 1. Load the data we prepared
wards = gpd.read_file("../../data/processed/my_wards_valid.gpkg")
stations = gpd.read_file("../../data/processed/my_stations_utm.gpkg")

# 2. Recreate the 2km buffer for the map
reach = stations.copy()
reach["geometry"] = reach.buffer(2000)

# 3. Create the plot
fig, ax = plt.subplots(figsize=(10, 10))

# Plot wards (background)
wards.plot(ax=ax, color="#f0f0f0", edgecolor="black", linewidth=0.5, label="Wards")

# Plot the 2km reach (light blue with transparency)
reach.plot(ax=ax, color="skyblue", alpha=0.4, label="2km Reach")

# Plot the police stations (red dots)
stations.plot(ax=ax, color="red", marker="^", markersize=50, label="Police Stations")

# Add title and legend
plt.title("Police Station Coverage in Maiduguri Wards", fontsize=16)
plt.legend(loc="lower left")
plt.axis("off") # Turn off the x/y axes for a cleaner map

# 4. Save the map as a PNG
plt.savefig("maiduguri_police_coverage.png", dpi=300, bbox_inches="tight")
print("Map successfully saved as maiduguri_police_coverage.png")